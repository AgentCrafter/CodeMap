# CodeMap

**CodeMap** is a Python-based tool designed to generate a hierarchical (tree-like) representation of your project's folder structure, allowing developers to quickly visualize internal organization while ignoring unnecessary files.

![Release Assets](assets/preview.png)

---

## Features

* 📂 Generates a clean tree structure of your project directory
* 🔍 Ignores clutter like `.git`, `__pycache__`, `.vscode`, and more
* 📝 Outputs result to a `summary_tree.txt` file
* ⚙️ Lightweight and dependency-free

---

## Installation

Clone the repository and install required dependencies:

```bash
git clone https://github.com/your-user/agentcrafter-codemap.git
cd agentcrafter-codemap
pip install -r requirements.txt
```

> The only required package is:
>
> ```
> gitingest
> ```

---

## Usage

### 📌 Option 1: Run with Python

```bash
python generate_tree.py
```

This will:

* Detect the current working directory
* Generate the tree
* Save it to `summary_tree.txt`

### 📌 Option 2: Run the Executable

Download `generate_tree.exe` from the [Releases](#releases) section and run it:

```bash
./generate_tree.exe
```

> ✅ Works out-of-the-box on Windows without Python.

---

## Example Output

```
📁 agentcrafter-codemap/
├── README.md
├── generate_tree.py
├── LICENSE
├── requirements.txt
└── im/
```

---

## Releases

Get the latest version from the [Releases](#) section:

* 🔧 [`generate_tree.exe`](#)
* 📦 Source code ([zip](#), [tar.gz](#))

---

## License

Licensed under the [Apache 2.0 License](LICENSE).
See the full license for more details.

---

## Contributing

Pull requests and suggestions are welcome!
For major changes, please open an issue first to discuss your ideas.
