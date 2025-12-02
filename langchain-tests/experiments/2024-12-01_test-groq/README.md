# Test Groq Models

Experimento para probar modelos de Groq con LangChain.

## Modelo usado

- **llama-3.3-70b-versatile**: Modelo rápido y versátil de Groq

## Otros modelos disponibles

```python
# Cambiar modelo en main.py:
llm = get_llm(provider='groq', model='llama-3.1-70b-versatile')  # Más potente
llm = get_llm(provider='groq', model='gemma2-9b-it')             # Más pequeño
```

## Ejecutar

```bash
python main.py
```

## Notas

- Groq es muy rápido para inferencia
- Requiere API key de Groq en `.env`
- Usa shared utilities para configuración
