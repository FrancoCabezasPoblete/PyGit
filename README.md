# Installation
Create virtual environment
```bash
python3.9 -m venv .venv
```

Active virtual environment
```bash
source venv/bin/activate
```

Install package
```bash
git clone https://github.com/FrancoCabezasPoblete/PyGit && pip install ./PyGit && rm -rf PyGit
```

# Program usage
```bash
pyget [command]
```

# Compile from source
Create virtual environment
```bash
python3.9 -m venv .venv
```

Active virtual environment
```bash
source venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

build package
```bash
pip install . && rm -rf build *.egg-info
```

