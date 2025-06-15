"""
Lord-Ugah-AI-v6 Ugahbase Creator Script

This script generates a new Ugahbase from the template, including .cursor-rules, index.md, and starter-note.md.
Prompts for Ugahbase name, creates the folder, copies template files, and updates the registry.
"""
import os
import shutil
# Dual import pattern: allows running as a module or as a script
try:
    from .utils import get_current_datetime  # module import
except ImportError:
    from utils import get_current_datetime   # script import

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UGAHBASES_DIR = os.path.join(ROOT, "ugahbases")
TEMPLATE_DIR = os.path.join(ROOT, "templates", "ugahbase-template")
REGISTRY_PATH = os.path.join(ROOT, "meta", "ugahbase-registry.md")


def prompt_ugahbase_name():
    name = input("Enter new Ugahbase name (kebab-case, e.g. 'machine-learning'): ").strip()
    if not name or not name.replace('-', '').isalnum():
        raise ValueError("Invalid Ugahbase name. Use kebab-case, alphanumeric and dashes only.")
    return name


def copy_template(dest_dir, ugahbase_name, current_datetime):
    os.makedirs(dest_dir, exist_ok=True)
    for fname in [".cursor-rules", "index.md", "starter-note.md"]:
        src = os.path.join(TEMPLATE_DIR, fname)
        if not os.path.exists(src):
            continue
        with open(src, "r") as f:
            content = f.read()
        # Replace placeholders
        content = content.replace("{{UGAHBASE_NAME}}", ugahbase_name.replace('-', ' ').title())
        content = content.replace("{{CURRENT_DATE}}", current_datetime)
        dest = os.path.join(dest_dir, fname if fname != "starter-note.md" else "starter-note.md")
        with open(dest, "w") as f:
            f.write(content)


def update_registry(ugahbase_name, current_datetime):
    entry = f"- {ugahbase_name} (created {current_datetime})\n"
    if not os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, "w") as f:
            f.write("# Ugahbase Registry\n\n")
    with open(REGISTRY_PATH, "a") as f:
        f.write(entry)


def main():
    print("[Lord-Ugah-AI-v6] Ugahbase Creator")
    try:
        name = prompt_ugahbase_name()
        dest_dir = os.path.join(UGAHBASES_DIR, name)
        if os.path.exists(dest_dir):
            print(f"Ugahbase '{name}' already exists.")
            return
        current_datetime = get_current_datetime()
        copy_template(dest_dir, name, current_datetime)
        update_registry(name, current_datetime)
        print(f"Ugahbase '{name}' created successfully at {dest_dir}.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main() 