# Project Setup Script for Python + VS Code

This script automates the creation of new Python project folders with:

- A virtual environment (`venv`)
- Git repository initialization
- Pre-configured `.gitignore`
- VS Code settings to auto-select the venv
- VS Code terminal that launches with the venv activated and prompt customized
- Optional `.activate.txt` and `.gitignore.txt` append support
- Auto-installation of the VS Code Python extension

## 📂 Directory Structure

When you run the script, it creates a structure like:

## 📂 Directory Structure

When you run the script, it creates a structure like:

```text
/opt/python/<project_name>/
├── venv/
├── main.py
├── .gitignore
├── .vscode/
│   ├── settings.json     ← from settings.json.txt
│   └── tasks.json        ← from tasks.json.txt
```

## 🚀 Usage

From terminal:

python3 make_new_project.py

You'll be prompted to enter a new project name. The script will then:

1. Create the project folder under /opt/python/
2. Set up a venv
3. Create main.py
4. Apply .gitignore, settings.json, and tasks.json templates
5. Open the project in VS Code

## 🔧 Required Files

Make sure these template files are in the same directory as the script:

- gitignore.txt → used for .gitignore
- settings.json.txt → VS Code interpreter + terminal profile
- tasks.json.txt → custom task to open a terminal with venv activated
- activate.txt (optional) → custom lines appended to venv/bin/activate

## 🧪 Confirming Venv Activation

Open a new terminal in VS Code, then run:

which python

It should return something like:

/opt/python/project_name/venv/bin/python

Your prompt should also begin with (venv) if configured correctly.

## 📦 Requirements

- Python 3.6+
- VS Code installed and accessible via `code`
- VS Code Python extension (auto-installed by the script)

## 📄 License

MIT License

