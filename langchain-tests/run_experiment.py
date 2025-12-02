#!/usr/bin/env python3
"""
Run an experiment from the project root
"""
import sys
import subprocess
from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser(description='Run a LangChain experiment')
    parser.add_argument('experiment', help='Experiment name (e.g., 2024-12-01_test-groq)')
    parser.add_argument('--script', default='main.py', help='Script to run (default: main.py)')
    
    args = parser.parse_args()
    
    # Get paths
    project_root = Path(__file__).parent
    exp_path = project_root / 'experiments' / args.experiment / args.script
    
    # Check if experiment exists
    if not exp_path.exists():
        print(f"❌ Error: Experiment script not found: {exp_path}")
        sys.exit(1)
    
    # Run the experiment with PYTHONPATH set to project root
    print(f"🚀 Running: {args.experiment}/{args.script}\n")
    
    env = {'PYTHONPATH': str(project_root)}
    result = subprocess.run(
        [sys.executable, str(exp_path)],
        cwd=str(project_root),
        env={**subprocess.os.environ, **env}
    )
    
    sys.exit(result.returncode)


if __name__ == '__main__':
    main()
