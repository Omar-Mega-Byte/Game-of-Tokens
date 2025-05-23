# Game-of-Tokens || Winter (error) is coming

A complete compiler frontend implementation featuring both a **lexical analyzer (lexer)** and a **parser** for a custom programming language. This project demonstrates fundamental compiler construction techniques in pure Python, providing a clean, well-structured foundation for language processing.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

## Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Language Syntax](#language-syntax)
* [Project Structure](#project-structure)
* [Development Roadmap](#development-roadmap)
* [Contributing](#contributing)
* [License](#license)

## Features

### ✅ Lexer

* Tokenizes source code into meaningful components
* Supports:

  * Keywords (`if`, `else`, `while`, etc.)
  * Identifiers and literals (numbers, strings, booleans)
  * Operators (arithmetic, logical, relational)
  * Comments (single-line and multi-line)
  * Punctuation and brackets
* Detailed error reporting with line numbers

### ✅ Parser

* Recursive descent parser implementation
* Constructs an Abstract Syntax Tree (AST)
* Detects and reports syntax errors with recovery
* Supports:

  * Variable declarations
  * Control flow structures (`if`, `else`, `while`)
  * Function definitions and calls
  * Basic expression parsing

### 🚧 Upcoming Features

* Type checking system
* REPL (Read-Eval-Print Loop) environment

## Installation

```bash
git clone https://github.com/yourusername/lexer-parser-project.git
cd lexer-parser-project
python --version  # Python 3.8+ required
pip install -r requirements.txt  # No external dependencies for now
```

## Usage

### Running the Lexer

```python
from lexer import Lexer

code = '''
if (x >= 5) {
    print("Hello");
}
'''

lexer = Lexer()
tokens, errors = lexer.tokenize(code)

for token in tokens:
    print(token)

if errors:
    print("\nErrors:")
    for error in errors:
        print(error)
```

### Running the Parser

```python
from parser import Parser
from lexer import Lexer

code = '''
function factorial(n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

let result = factorial(5);
print(result);
'''

lexer = Lexer()
tokens, errors = lexer.tokenize(code)

if errors:
    print("Lexical errors found:")
    for error in errors:
        print(error)
else:
    parser = Parser(tokens)
    ast = parser.parse()
    ast.pretty_print()  # Or whatever representation method your AST uses
```

## Language Syntax

```javascript
function factorial(n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

let result = factorial(5);
print(result);
```

## Project Structure

```
Project1/
├── src/
│   ├── lexer/
│   │   ├── __init__.py
│   │   ├── file_handler.py
│   │   ├── formatter.py
│   │   ├── keywords.py
│   │   └── lexer.py
│   │
│   ├── parser/
│   │   ├── __init__.py
│   │   ├── parser.py
│   │   ├── ast_nodes.py
│   │   └── syntax_rules.py
│   │
│   └── main.py
│
├── data/
│   ├── input/
│   └── output/
│
├── docs/
├── requirements.txt
└── README.md
```

## Development Roadmap

* [x] Complete lexer implementation
* [x] Implement basic parser
* [x] Add support for variable declarations
* [x] Implement control flow structures
* [x] Add function definitions and calls
* [ ] Develop type checking system
* [ ] Create REPL environment

## Contributing

Contributions are welcome!
Please follow the standard workflow:

1. Fork the repo
2. Create a branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## License

MIT License. See [LICENSE](LICENSE) for details.

---

**Note:** The parser is now available! Stay tuned for semantic analysis and type checking features coming next.

---
