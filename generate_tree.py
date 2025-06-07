import os

IGNORED_DIRS = {'.git', '__pycache__', 'venv', '.idea', '.vscode', 'node_modules'}
IGNORED_FILES = {'.DS_Store', 'summary_tree.txt', 'Screenshot.png', 'agentcrafter-codemap.txt'}
IGNORED_EXTENSIONS = {'.exe', '.code-workspace'}

def generate_tree(path='.', prefix=''):
    tree_output = []
    folders = []
    files = []

    for item in sorted(os.listdir(path)):
        if item in IGNORED_FILES:
            continue

        full_path = os.path.join(path, item)

        if os.path.isdir(full_path) and item not in IGNORED_DIRS:
            folders.append(item)
        elif os.path.isfile(full_path):
            ext = os.path.splitext(item)[1]
            if ext in IGNORED_EXTENSIONS:
                continue
            files.append(item)

    items = sorted(folders) + sorted(files)

    for index, item in enumerate(items):
        full_path = os.path.join(path, item)
        connector = '└── ' if index == len(items) - 1 else '├── '

        if os.path.isdir(full_path):
            tree_output.append(f"{prefix}{connector}📁 {item}/")
            extension = '    ' if index == len(items) - 1 else '│   '
            tree_output.extend(generate_tree(full_path, prefix + extension))
        else:
            tree_output.append(f"{prefix}{connector}{item}")

    return tree_output

def main():
    current_dir = os.getcwd()
    root_name = os.path.basename(current_dir)
    print(f"📂 Generating tree for: {root_name}\n")

    tree = [f"📁 {root_name}/"] + generate_tree()

    output_file = "summary_tree.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(tree))

    print(f"✅ Tree summary written to: {output_file}")

if __name__ == "__main__":
    main()
