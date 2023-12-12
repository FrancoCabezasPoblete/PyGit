# Compile from source
# Create virtual environment
python3.11.7 -m venv .venv

## Active virtual environment
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## build package
pip install . && rm -rf build *.egg-info

# Program usage
pyget [command]
