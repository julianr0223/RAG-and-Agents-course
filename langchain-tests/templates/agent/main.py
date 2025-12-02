"""
Agent experiment template
"""
from shared.config import get_llm
from shared.utils import print_section, print_response, print_success


def main():
    """Main agent experiment"""
    print_section("Agent Experiment")
    
    # TODO: Implement agent logic
    # 1. Define tools
    # 2. Create agent
    # 3. Run agent with task
    
    print("⚠️  Este es un template de ejemplo.")
    print("Implementa tu lógica de Agent aquí.\n")
    
    # Example structure:
    # from langchain.agents import create_react_agent, AgentExecutor
    # from langchain.tools import Tool
    # from langchain import hub
    
    print_success("Template cargado - listo para personalizar!")


if __name__ == "__main__":
    main()
