"""
Lord-Ugah-AI-v6 Ugahbase Creator Script

This script generates a new Ugahbase from the template, including .cursor-rules only.
Prompts for Ugahbase name, creates the folder, and copies template files.
"""
import os
import shutil
from utils import get_current_datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UGAHBASES_DIR = os.path.join(ROOT, "ugahbases")
TEMPLATE_DIR = os.path.join(ROOT, "templates", "ugahbase-template")


def prompt_ugahbase_name():
    name = input("Enter new Ugahbase name (kebab-case, e.g. 'machine-learning'): ").strip()
    if not name or not name.replace('-', '').isalnum():
        raise ValueError("Invalid Ugahbase name. Use kebab-case, alphanumeric and dashes only.")
    return name


def copy_template(dest_dir, ugahbase_name, current_datetime):
    os.makedirs(dest_dir, exist_ok=True)
    # Only copy .cursor-rules file
    src = os.path.join(TEMPLATE_DIR, ".cursor-rules")
    if os.path.exists(src):
        with open(src, "r") as f:
            content = f.read()
        # Replace placeholders
        content = content.replace("{{UGAHBASE_NAME}}", ugahbase_name.replace('-', ' ').title())
        content = content.replace("{{CURRENT_DATE}}", current_datetime)
        dest = os.path.join(dest_dir, ".cursor-rules")
        with open(dest, "w") as f:
            f.write(content)


# Registry functionality removed - filesystem provides this information


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
        print(f"Ugahbase '{name}' created successfully at {dest_dir}.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main() 