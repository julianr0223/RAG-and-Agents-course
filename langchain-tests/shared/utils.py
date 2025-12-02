"""
Shared utility functions for LangChain experiments
"""
from typing import Any


def print_response(response: Any, label: str = "Response"):
    """
    Pretty print a response from an LLM
    
    Args:
        response: Response object from LangChain
        label: Label to display before the response
    """
    print(f"\n{'='*60}")
    print(f"📝 {label}")
    print(f"{'='*60}")
    
    if hasattr(response, 'content'):
        print(response.content)
    else:
        print(response)
    
    print(f"{'='*60}\n")


def format_prompt(prompt: str, **kwargs) -> str:
    """
    Format a prompt with variables
    
    Args:
        prompt: Prompt template string
        **kwargs: Variables to substitute
    
    Returns:
        Formatted prompt
    """
    return prompt.format(**kwargs)


def print_section(title: str):
    """Print a section header"""
    print(f"\n{'='*60}")
    print(f"🚀 {title}")
    print(f"{'='*60}\n")


def print_success(message: str):
    """Print a success message"""
    print(f"✅ {message}")


def print_error(message: str):
    """Print an error message"""
    print(f"❌ {message}")
