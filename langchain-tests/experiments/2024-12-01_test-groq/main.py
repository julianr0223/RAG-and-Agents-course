"""
Test Groq models with LangChain
"""
from shared.config import get_llm
from shared.utils import print_section, print_response, print_success


def main():
    """Test Groq API with different models"""
    print_section("Testing Groq Models")
    
    # Initialize Groq LLM
    llm = get_llm(provider='groq', model='llama-3.3-70b-versatile')
    
    # Test prompt
    prompt = "¿Qué es LangChain en una oración?"
    
    print(f"🤖 Model: llama-3.3-70b-versatile")
    print(f"❓ Pregunta: {prompt}\n")
    
    # Invoke model
    response = llm.invoke(prompt)
    
    # Print response
    print_response(response, "Respuesta de Groq")
    
    print_success("Prueba de Groq completada!")


if __name__ == "__main__":
    main()
