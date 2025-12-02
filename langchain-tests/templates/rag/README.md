# RAG Experiment Template

Template para experimentos de Retrieval-Augmented Generation.

## Qué incluye

- Estructura básica para RAG
- Comentarios guía para implementación
- Integración con shared utilities

## Pasos típicos de RAG

1. **Cargar documentos**: TextLoader, PDFLoader, etc.
2. **Crear embeddings**: OpenAIEmbeddings, HuggingFaceEmbeddings
3. **Vector store**: FAISS, Chroma, Pinecone
4. **Retrieval**: Buscar documentos relevantes
5. **Generation**: Generar respuesta con contexto

## Dependencias adicionales

```bash
pip install faiss-cpu  # o faiss-gpu
pip install langchain-community
```
