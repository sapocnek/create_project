import os
import sys
import subprocess
from pathlib import Path

# --- CONFIGURATION ---
BASE_DIR = Path("/opt/python")  # project root
VSCODE_CMD = "code"
GITIGNORE_TEMPLATE = Path("gitignore.txt")
ACTIVATE_APPEND_FILE = Path("activate.txt")
SETTINGS_TEMPLATE = Path("settings.json.txt")
TASKS_TEMPLATE = Path("tasks.json.txt")
VSCODE_PYTHON_EXTENSION = "ms-python.python"

def ensure_vscode_python_extension():
    try:
        subprocess.run([VSCODE_CMD, "--install-extension", VSCODE_PYTHON_EXTENSION], check=True)
        print("🔌 Ensured VS Code Python extension is installed.")
    except subprocess.CalledProcessError:
        print("⚠️ Failed to install VS Code Python extension.")
    except FileNotFoundError:
        print(f"⚠️ Could not find '{VSCODE_CMD}'. Skipping extension check.")

def create_project(project_name):
    project_path = BASE_DIR / project_name
    venv_path = project_path / "venv"
    activate_path = venv_path / "bin" / "activate"

    # Create project directory
    project_path.mkdir(parents=True, exist_ok=False)
    print(f"📁 Created project folder: {project_path}")

    # Create virtual environment
    subprocess.run(["python3", "-m", "venv", str(venv_path)], check=True)
    print("🐍 Virtual environment created.")

    # Create starter Python file
    (project_path / "main.py").write_text('print("Hello from your new project!")\n')

    # Write .gitignore from template
    if GITIGNORE_TEMPLATE.exists():
        gitignore_content = GITIGNORE_TEMPLATE.read_text()
        (project_path / ".gitignore").write_text(gitignore_content)
        print("📄 .gitignore created from template.")
    else:
        print("⚠️ gitignore.txt not found. Skipping .gitignore creation.")

    # Append to venv/bin/activate from activate.txt
    if ACTIVATE_APPEND_FILE.exists() and activate_path.exists():
        with open(activate_path, "a") as f:
            f.write("\n# --- Appended by setup ---\n")
            f.write(ACTIVATE_APPEND_FILE.read_text())
        print("➕ Appended activate.txt to venv/bin/activate.")
    else:
        print("⚠️ activate.txt or venv/bin/activate not found. Skipping append.")

    # Create VS Code settings and tasks from templates
    vscode_dir = project_path / ".vscode"
    vscode_dir.mkdir(exist_ok=True)

    if SETTINGS_TEMPLATE.exists():
        (vscode_dir / "settings.json").write_text(SETTINGS_TEMPLATE.read_text())
        print("🛠️ VS Code settings.json created from settings.json.txt.")
    else:
        print("⚠️ settings.json.txt not found. Skipping VS Code settings.")

    if TASKS_TEMPLATE.exists():
        (vscode_dir / "tasks.json").write_text(TASKS_TEMPLATE.read_text())
        print("🧰 VS Code tasks.json created from tasks.json.txt.")
    else:
        print("⚠️ tasks.json.txt not found. Skipping VS Code tasks.")

    # Initialize Git repository
    subprocess.run(["git", "init"], cwd=project_path, check=True)
    print("🔧 Git repository initialized.")

    # Open in VS Code
    try:
        subprocess.run([VSCODE_CMD, str(project_path)])
        print("🚀 Project opened in VS Code.")
    except FileNotFoundError:
        print(f"⚠️ Could not find '{VSCODE_CMD}' command. Please open manually.")

if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        print("⚠️  You're currently inside a virtual environment. Please deactivate it before running this script.")
        exit(1)

    project = input("Enter new project name: ").strip()
    if not project:
        print("❌ Project name is required.")
    else:
        ensure_vscode_python_extension()
        try:
            create_project(project)
        except FileExistsError:
            print("❌ Project already exists.")
