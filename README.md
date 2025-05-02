# Game-of-Tokens || Winter (error) is coming
A complete compiler frontend implementation featuring a lexical analyzer (lexer) and upcoming parser/semantic analyzer for a custom programming language. This project demonstrates fundamental compiler construction techniques in pure Python, providing a clean, well-structured foundation for language processing.
# Lexer and Parser Project

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

A Python implementation of a lexical analyzer (lexer) and upcoming parser for a custom programming language.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Language Syntax](#language-syntax)
- [Project Structure](#project-structure)
- [Development Roadmap](#development-roadmap)
- [Contributing](#contributing)
- [License](#license)

## Features

### Current Lexer Implementation
- Tokenises source code into meaningful components
- Supports:
  - Keywords (`if`, `else`, `while`, etc.)
  - Identifiers and literals (numbers, strings, booleans)
  - Operators (arithmetic, logical, relational)
  - Comments (single-line and multi-line)
  - Punctuation and brackets
- Detailed error reporting with line numbers

### Planned Parser Features
- [ ] Recursive descent parser implementation
- [ ] Abstract Syntax Tree (AST) generation
- [ ] Syntax error detection and recovery
- [ ] Support for control structures and functions
- [ ] Type checking system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/lexer-parser-project.git
cd lexer-parser-project
```

2. Ensure you have Python 3.8+ installed:
```bash
python --version
```

3. Install dependencies (none currently required):
```bash
pip install -r requirements.txt
```

## Usage

### Running the Lexer
```python
from lexer import Lexer

code = """
if (x >= 5) { 
    print("Hello");
}
"""

lexer = Lexer()
tokens, errors = lexer.tokenize(code)

for token in tokens:
    print(token)

if errors:
    print("\nErrors:")
    for error in errors:
        print(error)
```

### Sample Output
```
Line 2: Token Text: if Token Type: IF
Line 2: Token Text: ( Token Type: BRACKET
Line 2: Token Text: x Token Type: IDENTIFIER
Line 2: Token Text: >= Token Type: REL_OP
Line 2: Token Text: 5 Token Type: INTEGER
...
```

## Language Syntax

```javascript
// Sample program that will be supported
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
│   └── main.py
│
├── data/
│   ├── input/
│   │   └── sample_input.txt 
│   │
│   └── output/
│       └── results.txt
|
├── docs/
│   ├── design.md
│   └── usage.md
│
├── requirements.txt
└── README.md
```

## Development Roadmap

- [x] Complete lexer implementation
- [ ] Implement basic parser
- [ ] Add support for variable declarations
- [ ] Implement control flow structures
- [ ] Add function definitions and calls
- [ ] Develop type system
- [ ] Create REPL environment

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:** This is an active development project. The parser implementation is coming soon! Check back regularly for updates.
