import os
import argparse
import tkinter as tk
from tkinter import filedialog

def create_directory_tree(dir_path, indent='', ignored_folders=[]):
    tree = ''
    items = os.listdir(dir_path)

    for index, item in enumerate(items):
        if item in ignored_folders:
            continue

        item_path = os.path.join(dir_path, item)
        is_last_item = index == len(items) - 1
        prefix = '└── ' if is_last_item else '├── '
        new_indent = indent + ('    ' if is_last_item else '│   ')

        tree += f"{indent}{prefix}{item}\n"

        if os.path.isdir(item_path):
            tree += create_directory_tree(item_path, new_indent, ignored_folders)

    return tree

def select_folder():
    root = tk.Tk()
    root.withdraw() 
    folder_selected = filedialog.askdirectory()
    return folder_selected


def main():
    base_ignored_folders = [
        'node_modules', '.git', 'dist', 'build', 'target', 'venv', 'env',
        '.tox', '.mypy_cache', '__pycache__', '.gradle', 'out', 'bower_components',
        '.next', '.nuxt'
    ]

    parser = argparse.ArgumentParser(description='Generar un árbol de directorios ASCII.')
    parser.add_argument('-i', '--ignore', nargs='*', help='Ignorar las carpetas base y las especificadas', default=[])
    parser.add_argument('-n', '--no-ignore', nargs='*', help='Ignorar solo las carpetas especificadas', default=[])
    args = parser.parse_args()

    if args.ignore:
        ignored_folders = base_ignored_folders + args.ignore
    elif args.no_ignore:
        ignored_folders = args.no_ignore
    else:
        ignored_folders = []

    folder_path = select_folder()
    if not folder_path:
        print("No folder selected")
        return
    
    tree = create_directory_tree(folder_path, ignored_folders=ignored_folders)
    print(tree)

if __name__ == "__main__":
    main()
