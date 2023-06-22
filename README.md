# LISP to AST Parser

This project is a simple LISP to Abstract Syntax Tree (AST) parser written in Python 3.11. 
It allows you to convert LISP code into an AST which is useful for a variety of purposes such as code analysis, optimization and execution.

## Installation

This guide will focus on installation on macOS.

### Python

Ensure you have Python 3.11 installed. You can check your Python version with:

```bash
python3 --version
```

If you don't have Python 3.11, you can install it using [pyenv](https://github.com/pyenv/pyenv):

```bash
brew install pyenv

pyenv install 3.11
pyenv global 3.11

echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
```

### Poetry

This project uses [Poetry](https://python-poetry.org/) for dependency management. If you don't have it, you can install it by running:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Project Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/timothepearce/lisp-ast.git
cd lisp-ast
```

2. Install the project dependencies with Poetry:

```bash
poetry install
```

## How to use

### Code

The main function in this project is `lisp_to_ast(code: str)`. You can use it as follows:

```python
from main import lisp_to_ast

code = '(print "Hello, June!")'
ast = lisp_to_ast(code)
print(ast)
```

This will output the AST representation of the LISP code:

```python
['print', 'Hello, June!']
```

### Execute tests

@todo Add a CLI to execute tests which are located in the "test_main.py" at the root of the project folder.

## Development process

### Methodology

Coming from a non-LISP background, the project began with researching LISP syntax and language features. The implementation was carried out using the Test-Driven Development (TDD) approach. The requirements were broken down into small, manageable parts - each defined by a specific test case. The test cases were written first, followed by the minimum amount of code required to pass those tests. This approach allows for more manageable development cycles, and helps ensure that all code has corresponding tests, leading to fewer bugs.
@todo add to this paragraph that I used the SBCL CLI to tests code before implementation (https://www.sbcl.org/)

### How the code works

The program takes a string of LISP code and breaks it down using regular expressions. 
This process is known as tokenization. Each token is then identified based on its pattern - e.g. number, keyword, string, etc. Once the code is tokenized, an Abstract Syntax Tree (AST) is built from the tokens. The AST is a tree representation of the code where each node is a token. It is built by analyzing the token list then group and nest them based on the LISP rules.
@todo reformat the above paragraph in a more technical explanation and better english.

## Technical Limitations

1. The parser Currently only supports a subset of LISP, including functions, arithmetic operators and primitive types. It doesn't support complex LISP features like macros or semaphores.

2. The parser is not optimized for performance and could be slow for large inputs.

3. The parser does not validate the syntax of the input LISP code. If the code is not valid LISP, the behavior of the parser is undefined. Future versions could include syntax validation to provide error messages for invalid LISP code.
