"""
Test HuggingFace models with LangChain
"""
from shared.config import get_llm
from shared.utils import print_section, print_response, print_success


def main():
    """Test HuggingFace API with models"""
    print_section("Testing HuggingFace Models")
    
    # Initialize HuggingFace LLM
    llm = get_llm(
        provider='huggingface',
        model='meta-llama/Llama-3.2-3B-Instruct',
        max_new_tokens=256,
        temperature=0.7
    )
    
    # Test prompt
    prompt = "¿Qué es LangChain en una oración?"
    
    print(f"🤖 Model: meta-llama/Llama-3.2-3B-Instruct")
    print(f"❓ Pregunta: {prompt}\n")
    
    # Invoke model
    response = llm.invoke(prompt)
    
    # Print response
    print_response(response, "Respuesta de HuggingFace")
    
    print_success("Prueba de HuggingFace completada!")


if __name__ == "__main__":
    main()
