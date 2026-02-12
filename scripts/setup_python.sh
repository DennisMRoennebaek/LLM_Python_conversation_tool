#!/usr/bin/env bash

set -e

echo "Checking Python installation (requires Python 3.11)..."

# Require Windows Python launcher (py) for reliable version selection
if ! command -v py &> /dev/null; then
  echo "The Windows Python launcher ('py') was not found."
  echo "Please install Python 3.11 from python.org and make sure it includes the launcher."
  exit 1
fi

# Verify Python 3.11 exists
if ! py -3.11 --version &> /dev/null; then
  echo "Python 3.11 not found."
  echo "Please install Python 3.11.x from python.org and re-run setup."
  exit 1
fi

PYTHON_CMD="py -3.11"

PYTHON_VERSION=$($PYTHON_CMD -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')")
echo "Detected Python: $PYTHON_VERSION"

# Hard requirement: 3.11.x
MAJOR=$($PYTHON_CMD -c "import sys; print(sys.version_info.major)")
MINOR=$($PYTHON_CMD -c "import sys; print(sys.version_info.minor)")

if [ "$MAJOR" -ne 3 ] || [ "$MINOR" -ne 11 ]; then
  echo "Python 3.11.x is required. Detected: $PYTHON_VERSION"
  exit 1
fi

echo "Python version OK."

# Create virtual environment if missing
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  $PYTHON_CMD -m venv .venv
else
  echo ".venv already exists."
fi

# Activate venv (Git Bash on Windows)
echo "Activating virtual environment..."
source .venv/Scripts/activate

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies
if [ -f "requirements.txt" ]; then
  echo "Installing Python dependencies..."
  pip install -r requirements.txt
else
  echo "requirements.txt not found. Skipping dependency install."
fi

echo ""
echo "Python environment ready."
