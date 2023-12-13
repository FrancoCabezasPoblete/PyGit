# Installation
Create virtual environment
```bash
python3.9 -m venv .venv
```

Active virtual environment
```bash
source .venv/bin/activate
```

Install package
```bash
git clone https://github.com/FrancoCabezasPoblete/PyGit && pip install ./PyGit && rm -rf PyGit
```

# Program usage
```bash
pygit [command] [options]
```

## Commands
- **commit**: Commit changes to the repository from the `commit_message.md` file. If the file does not exist, it will be created.

    `commit_message.md` file format:
    ```markdown
    <!--Title-->
    Here goes the title of the commit
    <!--Description-->
    Here goes the description of the commit
    ```

## Options
- **-h, --help**: Show help message and exit.
- **-p, --push**: Push changes to the remote repository.

# Compile from source
Create virtual environment
```bash
python3.9 -m venv .venv
```

Active virtual environment
```bash
source .venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

build package
```bash
pip install . && rm -rf build *.egg-info
```

