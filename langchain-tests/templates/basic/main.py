"""
Basic LangChain experiment template
"""
from shared.config import get_llm
from shared.utils import print_section, print_response, print_success


def main():
    """Main experiment function"""
    print_section("Basic LangChain Experiment")
    
    # Initialize LLM (change provider/model as needed)
    llm = get_llm(provider='groq', model='llama-3.3-70b-versatile')
    
    # Your prompt
    prompt = "¿Qué es LangChain en una oración?"
    
    print(f"Pregunta: {prompt}\n")
    
    # Invoke the model
    response = llm.invoke(prompt)
    
    # Print response
    print_response(response, "Respuesta del Modelo")
    
    print_success("Experimento completado!")


if __name__ == "__main__":
    main()
