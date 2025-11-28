# LangChain Tests - Curso de AI

Proyecto simple para probar diferentes modelos de IA con LangChain.

## Modelos Soportados
- **Groq**: Modelos rápidos (Llama 3.3, Llama 3.1, Gemma2)
- **HuggingFace**: Modelos open-source

## Setup Rápido

### 1. Crear entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar API Keys
Copia `.env.example` a `.env` y agrega tus API keys:
```bash
cp .env.example .env
```

Edita `.env` con tus keys:
- **Groq**: Obtén tu key en https://console.groq.com
- **HuggingFace**: Obtén tu key en https://huggingface.co/settings/tokens

### 4. Ejecutar pruebas

**IMPORTANTE:** Asegúrate de activar el entorno virtual primero:
```bash
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

Luego ejecuta los scripts:
```bash
# Probar Groq
python test_groq.py

# Probar HuggingFace
python test_huggingface.py
```

## Notas del Curso
- Groq es muy rápido para inferencia
- HuggingFace tiene muchos modelos gratuitos
- LangChain facilita cambiar entre modelos
