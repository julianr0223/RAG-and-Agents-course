#!/usr/bin/env python3
"""
CLI tool to create new LangChain experiments
"""
import os
import sys
import shutil
import argparse
from datetime import datetime
from pathlib import Path


# Available templates
TEMPLATES = {
    'basic': 'Basic LLM experiment',
    'rag': 'Retrieval-Augmented Generation',
    'agent': 'Agent with tools',
    'chain': 'LangChain chains',
}


def get_experiment_name(name: str) -> str:
    """Generate experiment folder name with date prefix"""
    date = datetime.now().strftime('%Y-%m-%d')
    return f"{date}_{name}"


def create_experiment(name: str, template: str = 'basic'):
    """
    Create a new experiment from template
    
    Args:
        name: Name of the experiment
        template: Template to use (basic, rag, agent, chain)
    """
    # Validate template
    if template not in TEMPLATES:
        print(f"❌ Error: Template '{template}' not found.")
        print(f"Available templates: {', '.join(TEMPLATES.keys())}")
        return False
    
    # Get paths
    project_root = Path(__file__).parent
    experiments_dir = project_root / 'experiments'
    template_dir = project_root / 'templates' / template
    
    # Create experiments directory if it doesn't exist
    experiments_dir.mkdir(exist_ok=True)
    
    # Generate experiment name with date
    exp_name = get_experiment_name(name)
    exp_dir = experiments_dir / exp_name
    
    # Check if experiment already exists
    if exp_dir.exists():
        print(f"❌ Error: Experiment '{exp_name}' already exists!")
        return False
    
    # Copy template to new experiment
    try:
        shutil.copytree(template_dir, exp_dir)
        print(f"✅ Created experiment: {exp_name}")
        print(f"📁 Location: {exp_dir}")
        print(f"\n🚀 To run your experiment:")
        print(f"   cd experiments/{exp_name}")
        print(f"   python main.py")
        return True
    except Exception as e:
        print(f"❌ Error creating experiment: {e}")
        return False


def list_templates():
    """List all available templates"""
    print("\n📋 Available Templates:\n")
    for name, description in TEMPLATES.items():
        print(f"  • {name:10} - {description}")
    print()


def list_experiments():
    """List all existing experiments"""
    project_root = Path(__file__).parent
    experiments_dir = project_root / 'experiments'
    
    if not experiments_dir.exists():
        print("No experiments found.")
        return
    
    experiments = sorted([d for d in experiments_dir.iterdir() if d.is_dir()])
    
    if not experiments:
        print("No experiments found.")
        return
    
    print(f"\n📚 Existing Experiments ({len(experiments)}):\n")
    for exp in experiments:
        print(f"  • {exp.name}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description='Create new LangChain experiments',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s my-test                    # Create basic experiment
  %(prog)s rag-demo --template rag    # Create RAG experiment
  %(prog)s --list-templates           # Show available templates
  %(prog)s --list                     # Show existing experiments
        """
    )
    
    parser.add_argument(
        'name',
        nargs='?',
        help='Name of the experiment (e.g., "test-prompts")'
    )
    
    parser.add_argument(
        '-t', '--template',
        default='basic',
        choices=list(TEMPLATES.keys()),
        help='Template to use (default: basic)'
    )
    
    parser.add_argument(
        '--list-templates',
        action='store_true',
        help='List available templates'
    )
    
    parser.add_argument(
        '--list',
        action='store_true',
        help='List existing experiments'
    )
    
    args = parser.parse_args()
    
    # Handle list commands
    if args.list_templates:
        list_templates()
        return
    
    if args.list:
        list_experiments()
        return
    
    # Create experiment
    if not args.name:
        parser.print_help()
        return
    
    create_experiment(args.name, args.template)


if __name__ == '__main__':
    main()
