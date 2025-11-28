"""
Test script para HuggingFace con LangChain
"""
import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Cargar variables de entorno
load_dotenv()

def test_huggingface():
    """Prueba básica con HuggingFace"""
    
    # Inicializar el modelo base
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.2-3B-Instruct",  # Modelo gratuito
        task="text-generation",
        huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
        max_new_tokens=256,
        temperature=0.7,
    )
    
    # Envolver en ChatHuggingFace para mejor compatibilidad
    chat_model = ChatHuggingFace(llm=llm)
    
    # Hacer una pregunta simple
    prompt = "¿Qué es LangChain en una oración?"
    
    print("🚀 Probando HuggingFace...")
    print(f"Pregunta: {prompt}\n")
    
    response = chat_model.invoke(prompt)
    
    print(f"Respuesta: {response.content}\n")
    print("✅ Prueba completada!")

if __name__ == "__main__":
    test_huggingface()
