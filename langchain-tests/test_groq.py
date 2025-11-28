"""
Test script para Groq con LangChain
"""
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Cargar variables de entorno
load_dotenv()

def test_groq():
    """Prueba básica con Groq"""
    
    # Inicializar el modelo
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile"  # Otros modelos: llama-3.1-70b-versatile, gemma2-9b-it
    )
    
    # Hacer una pregunta simple
    prompt = "¿Qué es LangChain en una oración?"
    
    print("🚀 Probando Groq...")
    print(f"Pregunta: {prompt}\n")
    
    response = llm.invoke(prompt)
    
    print(f"Respuesta: {response.content}\n")
    print("✅ Prueba completada!")

if __name__ == "__main__":
    test_groq()
