import re
from typing import Any


def tokenize(code: str) -> list[Any]:
    pattern = re.compile(r'\s*(\(|\)|"[^"]*"|[^\s()]+)\s*')
    return pattern.findall(code)


def parse_tokens(tokens: list[any]) -> list[Any]:
    return tokens


def lisp_to_ast(code: str) -> list[str]:
    tokens = tokenize(code)
    ast = parse_tokens(tokens)
    return ast
