"""
Shared configuration for LangChain experiments
"""
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


def load_api_keys():
    """Load API keys from .env file"""
    load_dotenv()
    return {
        'groq': os.getenv('GROQ_API_KEY'),
        'huggingface': os.getenv('HUGGINGFACE_API_KEY'),
    }


def get_llm(provider='groq', model=None, **kwargs):
    """
    Get a configured LLM instance
    
    Args:
        provider: 'groq' or 'huggingface'
        model: Model name (optional, uses defaults if not provided)
        **kwargs: Additional arguments to pass to the LLM
    
    Returns:
        Configured LLM instance
    """
    load_dotenv()
    
    if provider == 'groq':
        model = model or 'llama-3.3-70b-versatile'
        return ChatGroq(
            api_key=os.getenv('GROQ_API_KEY'),
            model=model,
            **kwargs
        )
    
    elif provider == 'huggingface':
        model = model or 'meta-llama/Llama-3.2-3B-Instruct'
        llm = HuggingFaceEndpoint(
            repo_id=model,
            task='text-generation',
            huggingfacehub_api_token=os.getenv('HUGGINGFACE_API_KEY'),
            max_new_tokens=kwargs.get('max_new_tokens', 256),
            temperature=kwargs.get('temperature', 0.7),
        )
        return ChatHuggingFace(llm=llm)
    
    else:
        raise ValueError(f"Unknown provider: {provider}")


# Common model configurations
MODELS = {
    'groq': {
        'fast': 'llama-3.3-70b-versatile',
        'powerful': 'llama-3.1-70b-versatile',
        'small': 'gemma2-9b-it',
    },
    'huggingface': {
        'default': 'meta-llama/Llama-3.2-3B-Instruct',
    }
}
