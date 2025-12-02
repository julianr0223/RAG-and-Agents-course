# Agent Experiment Template

Template para experimentos con LangChain Agents.

## Qué incluye

- Estructura básica para agents
- Comentarios guía para implementación
- Integración con shared utilities

## Conceptos de Agents

- **Tools**: Funciones que el agent puede usar
- **Agent**: Decide qué tool usar y cuándo
- **Executor**: Ejecuta las decisiones del agent

## Ejemplo básico

```python
from langchain.agents import Tool, create_react_agent
from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calcula expresiones matemáticas"""
    return str(eval(expression))

# Crear agent con tools
```
