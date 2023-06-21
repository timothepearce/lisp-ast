import re

Token = tuple[str, str]
ASTNode = str | int | list["ASTNode"]

TOKEN_LEFT_PARENTHESIS = "LPAREN"
TOKEN_RIGHT_PARENTHESIS = "RPAREN"
TOKEN_KEYWORD = "KEYWORD"
TOKEN_NUMBER = "NUMBER"
TOKEN_STRING = "STRING"
TOKEN_OPERATOR = "OPERATOR"
TOKEN_IDENTIFIER = "IDENTIFIER"

REGEX_KEYWORD = r"\b(defun|lambda|if|then|else|let|print|first|list)\b"
REGEX_NUMBER = r"\d+"
REGEX_STRING = r'"(?:[^"\\]|\\.)*"'
REGEX_OPERATOR = r"(<=|>=|<|>|=|\*|\+|-|/)"
REGEX_IDENTIFIER = r"\b[a-zA-Z][a-zA-Z0-9]*\b"


def tokenize(code: str) -> list[Token]:
    pattern = re.compile(r'\s*(\(|\)|"[^"]*"|[^\s()]+)\s*')
    tokens = pattern.findall(code)
    return [(match_token_type(token), token) for token in tokens]


def match_token_type(token: str) -> str:
    if token == "(":
        return TOKEN_LEFT_PARENTHESIS
    elif token == ")":
        return TOKEN_RIGHT_PARENTHESIS
    elif re.fullmatch(REGEX_KEYWORD, token):
        return TOKEN_KEYWORD
    elif re.fullmatch(REGEX_NUMBER, token):
        return TOKEN_NUMBER
    elif re.fullmatch(REGEX_STRING, token):
        return TOKEN_STRING
    elif re.fullmatch(REGEX_OPERATOR, token):
        return TOKEN_OPERATOR
    elif re.fullmatch(REGEX_IDENTIFIER, token):
        return TOKEN_IDENTIFIER
    else:
        raise ValueError(f"Invalid token: {token}")


def build_ast(tokens: list[Token]) -> list[ASTNode]:
    token_iter = iter(tokens)

    def parse_expression():
        node = []
        for token_type, value in token_iter:
            if token_type == TOKEN_LEFT_PARENTHESIS:
                node.append(parse_expression())
            elif token_type == TOKEN_RIGHT_PARENTHESIS:
                return node
            elif token_type == TOKEN_NUMBER:
                node.append(int(value))
            elif token_type == TOKEN_STRING:
                node.append(value.strip('"'))
            else:
                node.append(value)
        return node

    return parse_expression()[0]


def lisp_to_ast(code: str) -> list[str]:
    tokens = tokenize(code)
    return build_ast(tokens)
