"""
Chain experiment template
"""
from shared.config import get_llm
from shared.utils import print_section, print_response, print_success
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def main():
    """Main chain experiment"""
    print_section("Chain Experiment - Platos Típicos")

    # Initialize Groq LLM
    llm = get_llm(provider='groq', model='llama-3.3-70b-versatile')
    parser = StrOutputParser()
    
    # Chain 1 - Meal
    prompt_meal = ChatPromptTemplate.from_template("Tu trabajo es darme UN solo nombre de un plato típico de {pais}. Solo el nombre.")
    chain_meal = prompt_meal | llm | parser
    
    # Chain 2 - Recipe
    prompt_recipe = ChatPromptTemplate.from_template("Dado este plato: {meal}, dame una receta MUY corta (máximo 3 líneas) para hacerlo en casa.")
    chain_recipe = prompt_recipe | llm | parser
    
    # Chain 3 - Time
    prompt_time = ChatPromptTemplate.from_template("Dada esta receta: {recipe}, estima cuánto tiempo toma cocinarlo. Responde solo con el tiempo (ej: '30 mins').")
    chain_time = prompt_time | llm | parser

    # Execute chains sequentially
    full_chain = (
        # 1. Calculamos 'meal' y lo guardamos en el estado. Input inicial: {pais}
        RunnablePassthrough.assign(meal=chain_meal)
        
        # 2. Ahora el estado es {pais, meal}. Calculamos 'recipe'.
        | RunnablePassthrough.assign(recipe=chain_recipe)
        
        # 3. Ahora el estado es {pais, meal, recipe}. Calculamos 'time'.
        | RunnablePassthrough.assign(time=chain_time)
    )

    print("🚀 Ejecutando pipeline...")
    response = full_chain.invoke({"pais": "Colombia"})
    
    print("\n📊 RESULTADO FINAL ESTRUCTURADO:")
    print(f"🌎 País:   {response['pais']}")
    print(f"🥘 Plato:  {response['meal']}")
    print(f"📝 Receta: {response['recipe']}")
    print(f"⏱️ Tiempo: {response['time']}")
    

if __name__ == "__main__":
    main()
