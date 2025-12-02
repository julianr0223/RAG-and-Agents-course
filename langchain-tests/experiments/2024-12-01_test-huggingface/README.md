# Test HuggingFace Models

Experimento para probar modelos de HuggingFace con LangChain.

## Modelo usado

- **meta-llama/Llama-3.2-3B-Instruct**: Modelo gratuito de HuggingFace

## Configuración

```python
llm = get_llm(
    provider='huggingface',
    model='meta-llama/Llama-3.2-3B-Instruct',
    max_new_tokens=256,
    temperature=0.7
)
```

## Ejecutar

```bash
python main.py
```

## Notas

- HuggingFace tiene muchos modelos gratuitos
- Requiere API key de HuggingFace en `.env`
- Usa shared utilities para configuración
- Puede ser más lento que Groq
