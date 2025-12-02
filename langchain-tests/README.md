# LangChain Experiments - Sistema Dinámico

Proyecto flexible para experimentar con diferentes conceptos de LangChain. Crea experimentos bajo demanda usando templates predefinidos.

## 🚀 Quick Start

### 1. Configurar Entorno

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar API keys
cp .env.example .env
# Edita .env con tus API keys
```

### 2. Crear un Nuevo Experimento

```bash
# Experimento básico
python new_experiment.py mi-prueba

# Con template específico
python new_experiment.py rag-test --template rag
python new_experiment.py agent-demo --template agent
python new_experiment.py chain-test --template chain

# Ver templates disponibles
python new_experiment.py --list-templates

# Ver experimentos existentes
python new_experiment.py --list
```

### 3. Ejecutar un Experimento

```bash
# Opción 1: Usar el runner (recomendado)
python3 run_experiment.py 2024-12-01_test-groq

# Opción 2: Desde la raíz del proyecto
source venv/bin/activate
PYTHONPATH=. python3 experiments/2024-12-01_test-groq/main.py
```

## 📁 Estructura del Proyecto

```
langchain-tests/
├── experiments/              # Tus experimentos (creados dinámicamente)
│   ├── 2024-12-01_test-groq/
│   ├── 2024-12-01_test-huggingface/
│   └── ...
├── shared/                   # Código compartido
│   ├── config.py            # Configuración y factory de LLMs
│   └── utils.py             # Funciones de utilidad
├── templates/               # Templates para nuevos experimentos
│   ├── basic/              # LLM básico
│   ├── rag/                # Retrieval-Augmented Generation
│   ├── agent/              # Agents con tools
│   └── chain/              # LangChain chains
├── data/                    # Datos de prueba
├── new_experiment.py        # CLI para crear experimentos
├── .env                     # API keys (no commitear)
└── requirements.txt         # Dependencias Python
```

## 🎯 Templates Disponibles

### Basic
Experimento simple con un modelo LLM.
```bash
python new_experiment.py test-basic --template basic
```

### RAG (Retrieval-Augmented Generation)
Template para experimentos con vectorstores y retrieval.
```bash
python new_experiment.py rag-demo --template rag
```

### Agent
Template para agents con tools personalizadas.
```bash
python new_experiment.py agent-test --template agent
```

### Chain
Template para LangChain chains y prompt templates.
```bash
python new_experiment.py chain-demo --template chain
```

## 🛠️ Código Compartido

Todos los experimentos pueden usar las utilidades compartidas:

```python
from shared.config import get_llm
from shared.utils import print_response, print_section

# Obtener LLM configurado
llm = get_llm(provider='groq')  # o 'huggingface'

# Usar utilidades
print_section("Mi Experimento")
response = llm.invoke("¿Qué es LangChain?")
print_response(response)
```

### Modelos Disponibles

**Groq** (rápido):
```python
llm = get_llm(provider='groq', model='llama-3.3-70b-versatile')
llm = get_llm(provider='groq', model='llama-3.1-70b-versatile')
llm = get_llm(provider='groq', model='gemma2-9b-it')
```

**HuggingFace** (gratuito):
```python
llm = get_llm(provider='huggingface', model='meta-llama/Llama-3.2-3B-Instruct')
```

## 📝 Workflow Recomendado

1. **Crear experimento**: `python3 new_experiment.py nombre-descriptivo --template tipo`
2. **Editar código**: Modifica `experiments/YYYY-MM-DD_nombre/main.py`
3. **Ejecutar**: `python3 run_experiment.py YYYY-MM-DD_nombre`
4. **Documentar**: Agrega notas en el `README.md` del experimento

## 🔑 API Keys

Obtén tus API keys:
- **Groq**: https://console.groq.com
- **HuggingFace**: https://huggingface.co/settings/tokens

Agrégalas a `.env`:
```bash
GROQ_API_KEY=tu_key_aqui
HUGGINGFACE_API_KEY=tu_key_aqui
```

## 💡 Tips

- Los experimentos se nombran automáticamente con fecha: `YYYY-MM-DD_nombre`
- Cada experimento es independiente y autocontenido
- Usa `shared/` para código que quieras reutilizar
- Los templates son solo puntos de partida, personalízalos libremente

## 📚 Recursos

- [LangChain Docs](https://python.langchain.com/)
- [Groq API](https://console.groq.com/docs)
- [HuggingFace Hub](https://huggingface.co/docs/hub)
