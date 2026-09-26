# Python Learning

A personal collection of Python scripts and exercises documenting my journey learning Python from the ground up — starting with the basics of syntax and variables, and progressing through data structures, functions, file handling, and object-oriented programming.

> 📚 Each file is numbered in the order the topic was learned, so the repo doubles as a step-by-step course log.

## About

This repository is **not a single application** but a series of standalone `.py` scripts, each focused on one Python concept or a small practice exercise. It's meant to track progress and serve as a personal reference to revisit fundamentals and see how understanding has grown over time.

## Topics Covered

### Basics & Syntax
- Introduction to programming & Python, first program, comments and escape sequences
- Variables, data types, type casting
- Taking user input, strings, string slicing & methods, f-strings, docstrings

### Control Flow
- If/else conditionals, match-case statements
- For loops, while loops, break & continue, for-loop with else

### Functions
- Functions and function arguments
- Lambda functions
- Map, filter, reduce
- `is` vs `==`

### Data Structures
- Lists and list methods
- Tuples and tuple operations
- Sets and set methods
- Dictionaries and dictionary methods

### Error Handling
- Exception handling, `finally` keyword, raising custom errors

### Modules & Environment
- Modules and pip
- How imports work in Python
- Virtual environments
- `os` module
- `if __name__ == "__main__"`
- Local vs global variables

### File Handling
- File I/O basics
- `read()`, `readlines()`, and other file methods
- `seek()`, `tell()`, and related methods

### Object-Oriented Programming (OOP)
- Introduction to OOP, classes and objects, constructors
- Getters and setters, access modifiers
- Static methods, class methods, instance vs. class variables
- Class methods as alternative constructors
- Inheritance: single, multiple, multilevel, hierarchical & hybrid
- `super()` keyword, method overriding
- Magic/dunder methods, `dir()`, `__dict__`, and `help()`

### Practice Exercises & Mini Projects
- Calculator using Python
- "Kaun Banega Crorepati" quiz game (with solution)
- Snake, Water, Gun game (with solution)
- Library management system
- Command-line utility
- PDF merging exercise (with solution)
- Time module usage
- Assorted "clear the clutter" and custom dictionary exercises

## Repository Structure

```
Python-Learning/
├── 1IntoductionToProgrammingAndPython.py
├── 2SomeAmazingPythonPrograms.py
├── 3ModulesAndPip.py
├── ...
├── 85commandLineUtility.py
├── Talha2/11S/            # additional practice folder
├── clutter/               # practice/exercise files
├── jupiter/                # Jupyter-related experiments
├── __pycache__/            # compiled Python cache (auto-generated)
└── *.txt, *.pdf             # sample files used in file-I/O and PDF exercises
```

Files are numbered in the rough order topics were learned (e.g., `1...py` through `85...py`), so reading them in numeric order roughly follows a beginner-to-intermediate Python curriculum.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/TalhaHabib-hub/Python-Learning.git
   cd Python-Learning
   ```

2. **Make sure Python 3 is installed**
   ```bash
   python --version
   ```

3. **Run any script directly**
   ```bash
   python 20FunctionsInPython.py
   ```

Some scripts (e.g., the PDF-merging exercise) may require external packages. If a script fails with a `ModuleNotFoundError`, install the missing package with:
```bash
pip install <package-name>
```

## Purpose

This repository serves as:
- A **learning log** tracking progress through core Python concepts
- A **quick reference** to revisit specific topics (loops, OOP, file handling, etc.)
- A **practice ground** for small coding exercises and mini projects

## Contributing

This is a personal learning repository and isn't actively seeking contributions. That said, feel free to explore, fork, or open an issue if you spot something worth discussing.

## License

No license specified. Feel free to reach out to the repository owner if you'd like to use any part of this code.

## Author

**Talha Habib** — [@TalhaHabib-hub](https://github.com/TalhaHabib-hub)
