# Utilisation

- Cloner le repo / mettre en place un workspace vide contenant uniquement le fichier Python à packager (ex: `morpion.py`).
- Dans ce workspace, ajouter le script `make_project.py` (fourni dans ce repo).
- Ouvrir un terminal dans le dossier courant.

---

# Exécution

## Commande de base

```cmd
python make_project.py morpion.py
```

---

## Commande avec venv personnalisé (optionnel)

```cmd
python make_project.py morpion.py nom_du_venv
```

---

# Ce que fait le script automatiquement

## Structure du projet

Le script crée une architecture Python standard :

```
src/<nom_du_module>/
tests/
```

Puis il déplace automatiquement le fichier Python fourni vers :

```
src/<nom_du_module>/<fichier>.py
```

---

## Environnement virtuel (venv)

Le script :

- Crée un environnement virtuel dans le dossier courant :
  - `venv/` par défaut
  - ou un nom personnalisé si fourni en argument
- Initialise pip automatiquement
- Installe dans le venv :
  - pip (mise à jour)
  - build
  - twine
  - pytest

---

## Configuration du projet

Le script génère automatiquement :

- `pyproject.toml`
- `README.md`
- `.gitignore`
- `LICENSE` (vide par défaut)
- `__init__.py`
- fichier de test : `tests/test_<module>.py`

---

# Activation du venv

Après exécution du script, activer l’environnement virtuel manuellement :

## Windows

```cmd
venv\Scripts\activate
```

## Mac / Linux

```bash
source venv/bin/activate
```

---

# Nettoyage

Supprimer le fichier `make_project.py` du workspace après utilisation afin d’éviter tout conflit ou réexécution accidentelle.

---

# Remarques

- La commande `python` peut varier selon l’installation :
  - `python`
  - `python3`
  - `py` (Windows)

- Le venv créé est automatiquement ignoré via `.gitignore` si généré par le script.
