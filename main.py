import re
from typing import Any

TOKEN_LEFT_PARENTHESIS = "LPAREN"
TOKEN_RIGHT_PARENTHESIS = "RPAREN"
TOKEN_KEYWORD = "KEYWORD"
TOKEN_NUMBER = "NUMBER"
TOKEN_STRING = "STRING"
TOKEN_OPERATOR = "OPERATOR"
TOKEN_SYMBOL = "SYMBOL"

LEFT_PARENTHESIS = "("
RIGHT_PARENTHESIS = ")"
REGEX_KEYWORD = r"\b(defun|lambda|if|then|else|let|print|first|list)\b"
REGEX_NUMBER = r"\d+"
REGEX_STRING = r'"(?:[^"\\]|\\.)*"'
REGEX_OPERATOR = r'[<>=*+-/]'
REGEX_SYMBOL = r"[^\s\(\)]+"


def tokenize(code: str) -> list[Any]:
    pattern = re.compile(r'\s*(\(|\)|"[^"]*"|[^\s()]+)\s*')
    tokens = pattern.findall(code)
    return [(match_token_type(token), token) for token in tokens]


def match_token_type(token: str) -> str:
    if token == LEFT_PARENTHESIS:
        return TOKEN_LEFT_PARENTHESIS
    elif token == RIGHT_PARENTHESIS:
        return TOKEN_RIGHT_PARENTHESIS
    elif re.fullmatch(REGEX_KEYWORD, token):
        return TOKEN_KEYWORD
    elif re.fullmatch(REGEX_NUMBER, token):
        return TOKEN_NUMBER
    elif re.fullmatch(REGEX_STRING, token):
        return TOKEN_STRING
    elif re.fullmatch(REGEX_OPERATOR, token):
        return TOKEN_OPERATOR
    elif re.fullmatch(REGEX_SYMBOL, token):
        return TOKEN_SYMBOL
    else:
        raise ValueError(f"Invalid token: {token}")


def parse_tokens(tokens: list[any]) -> list[Any]:
    return tokens


def lisp_to_ast(code: str) -> list[str]:
    tokens = tokenize(code)
    ast = parse_tokens(tokens)
    return ast
