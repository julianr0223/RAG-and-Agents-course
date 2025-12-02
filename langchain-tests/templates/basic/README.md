# Basic LangChain Experiment

Template básico para experimentos con modelos LLM.

## Qué incluye

- Configuración simple de LLM (Groq o HuggingFace)
- Ejemplo de prompt básico
- Uso de utilidades compartidas

## Cómo usar

1. Modifica el `prompt` en `main.py`
2. Cambia el modelo si lo deseas (provider, model)
3. Ejecuta: `python main.py`

## Personalización

```python
# Cambiar a HuggingFace
llm = get_llm(provider='huggingface')

# Usar modelo específico
llm = get_llm(provider='groq', model='gemma2-9b-it')
```
