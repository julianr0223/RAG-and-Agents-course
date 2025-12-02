# Chain Experiment - Platos Típicos

Experimento para probar LangChain Chains con prompt templates usando **LCEL** (LangChain Expression Language).

## ¿Qué hace este experimento?

Usa **LCEL** (el nuevo estándar de LangChain) para crear una chain que genera platos típicos de diferentes países usando un prompt template.

## Conceptos de LangChain

### PromptTemplate
Define un template con variables que se pueden reemplazar:
```python
from langchain_core.prompts import PromptTemplate

template = "Tu trabajo es darme un plato típico de {pais}."
prompt = PromptTemplate.from_template(template)
```

### LCEL (LangChain Expression Language)
La forma moderna de crear chains en LangChain usando el operador `|`:
```python
# Crear chain con LCEL
chain = prompt_template | llm

# Ejecutar
result = chain.invoke({"pais": "Argentina"})
print(result.content)
```

> **Nota:** `LLMChain` está deprecado en LangChain 1.1.0+. Usa LCEL en su lugar.

## Cómo ejecutar

### Paso 1: Asegúrate de tener el entorno activado
```bash
source venv/bin/activate
```

### Paso 2: Ejecuta el experimento

**Opción 1: Usando el runner (recomendado)**
```bash
python3 run_experiment.py 2025-12-01_chain_test_mod2
```

**Opción 2: Manualmente desde la raíz**
```bash
PYTHONPATH=. python3 experiments/2025-12-01_chain_test_mod2/main.py
```

## Salida esperada

```
============================================================
🚀 Chain Experiment - Platos Típicos
============================================================

🌎 Consultando plato típico de Argentina...

============================================================
📝 Plato Típico
============================================================
Asado de Tira: Un plato tradicional argentino consistente en 
tiras de carne de vaca asadas a la parrilla...
============================================================

✅ Chain ejecutada correctamente!
```

## Dependencias

Este experimento usa:
- `langchain-core` - Para PromptTemplate y LCEL
- `shared.config` - Para obtener el LLM configurado
- `shared.utils` - Para formateo de salida

## Personalización

Puedes modificar el template o probar con diferentes países:

```python
# Cambiar el prompt
template = "Dame una receta completa de {pais} con ingredientes."

# Probar con diferentes países
result = chain.invoke({"pais": "México"})
result = chain.invoke({"pais": "Italia"})
result = chain.invoke({"pais": "Japón"})
```

## Notas del Módulo 2

- **LCEL** es el nuevo estándar para crear chains (usa `|`)
- **PromptTemplate** hace los prompts reutilizables
- `LLMChain` está deprecado, usa LCEL en su lugar
- Los imports ahora son de `langchain_core` en vez de `langchain`
