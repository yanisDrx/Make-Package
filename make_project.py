import sys
from pathlib import Path
import shutil

def create_structure(file_path: str):
    root = Path.cwd()
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"Fichier introuvable: {file_path}")
        return

    # nom du module = nom du fichier sans .py
    module_name = file_path.stem

    # création structure
    src_pkg = root / "src" / module_name
    tests = root / "tests"

    src_pkg.mkdir(parents=True, exist_ok=True)
    tests.mkdir(parents=True, exist_ok=True)

    # déplacer le fichier existant dans src/
    new_file_path = src_pkg / file_path.name
    shutil.move(str(file_path), str(new_file_path))

    print(f"Fichier déplacé vers: {new_file_path}")

    # créer __init__.py
    (src_pkg / "__init__.py").write_text("")

    # créer fichier de test
    (tests / f"test_{module_name}.py").write_text(
        f"# tests pour {module_name}\n"
    )

    # fichiers racine
    (root / "README.md").write_text(f"# {module_name}\n")
    (root / ".gitignore").write_text("__pycache__/\n*.pyc\n")

    (root / "pyproject.toml").write_text(f"""
[project]
name = "{module_name}"
version = "0.1.0"
""".strip())

    print(f"Structure créée pour {module_name} 🚀")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python make_project.py fichier.py")
    else:
        create_structure(sys.argv[1])