# Chain Experiment Template

Template para experimentos con LangChain Chains.

## Qué incluye

- Estructura básica para chains
- Comentarios guía para implementación
- Integración con shared utilities

## Tipos de Chains

- **LLMChain**: Chain simple con prompt template
- **SequentialChain**: Encadena múltiples chains
- **RouterChain**: Enruta a diferentes chains según input

## Ejemplo básico

```python
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

template = "Traduce al {idioma}: {texto}"
prompt = PromptTemplate(template=template, input_variables=["idioma", "texto"])

chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(idioma="inglés", texto="Hola mundo")
```
