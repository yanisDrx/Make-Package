import sys
from pathlib import Path
import shutil
import subprocess
import venv

def run(cmd):
    print(">>", " ".join(cmd))
    subprocess.check_call(cmd)

def create_structure(file_path: str, venv_name: str = "venv"):
    root = Path.cwd()
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"Fichier introuvable: {file_path}")
        return

    # nom du module = nom du fichier sans .py
    module_name = file_path.stem

    # =========================
    # STRUCTURE DU PROJET
    # =========================
    src_pkg = root / "src" / module_name
    tests = root / "tests"

    src_pkg.mkdir(parents=True, exist_ok=True)
    tests.mkdir(parents=True, exist_ok=True)

    # déplacer fichier source
    new_file_path = src_pkg / file_path.name
    shutil.move(str(file_path), str(new_file_path))

    print(f"Fichier déplacé vers: {new_file_path}")

    # =========================
    # FICHIERS PYTHON PACKAGING
    # =========================
    (src_pkg / "__init__.py").write_text("")

    (tests / f"test_{module_name}.py").write_text(
        f"# tests pour {module_name}\n"
    )

    # =========================
    # FICHIERS ROOT
    # =========================
    (root / "README.md").write_text(f"# {module_name}\n")

    (root / "LICENSE").write_text("")

    (root / "pyproject.toml").write_text(f"""
[project]
name = "{module_name}"
version = "0.1.0"
description = ""
""".strip())

    # =========================
    # VENV
    # =========================
    venv_path = root / venv_name
    print(f"Création du venv: {venv_name}")

    venv.create(venv_path, with_pip=True)

    # python du venv (Windows / Linux / Mac)
    python_bin = venv_path / "Scripts" / "python.exe"
    if not python_bin.exists():
        python_bin = venv_path / "bin" / "python"

    # =========================
    # INSTALL PIP PACKAGES
    # =========================
    run([str(python_bin), "-m", "pip", "install", "--upgrade", "pip"])
    run([str(python_bin), "-m", "pip", "install", "build", "twine", "pytest"])

    # =========================
    # GITIGNORE
    # =========================
    (root / ".gitignore").write_text(f"""
{venv_name}/
__pycache__/
*.pyc
""".strip())

    print("Structure créée avec succès 🚀")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python make_project.py fichier.py [venv_name]")
    else:
        file = sys.argv[1]
        venv_name = sys.argv[2] if len(sys.argv) > 2 else "venv"
        create_structure(file, venv_name)
