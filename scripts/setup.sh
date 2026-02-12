#!/usr/bin/env bash

set -e

echo "======================================"
echo "Voice Local LLM — Environment Setup"
echo "======================================"

# Ensure runtime directory exists
mkdir -p runtime

# Python environment
bash scripts/setup_python.sh

# Run individual installers
bash scripts/setup_piper.sh

# Future:
# bash scripts/setup_models.sh
# bash scripts/setup_ollama.sh

echo ""
echo "Setup complete."
echo "You can now run:"
echo "python main.py"
