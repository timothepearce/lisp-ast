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

TOKENS = {
    TOKEN_LEFT_PARENTHESIS: r"\(",
    TOKEN_RIGHT_PARENTHESIS: r"\)",
    TOKEN_KEYWORD: r"\b(defun|lambda|if|then|else|let|print|first|list)\b",
    TOKEN_NUMBER: r"\d+",
    TOKEN_STRING: r'"(?:[^"\\]|\\.)*"',
    TOKEN_OPERATOR: r"(<=|>=|<|>|=|\*|\+|-|/)",
    TOKEN_IDENTIFIER: r"\b[a-zA-Z][a-zA-Z0-9]*\b"
}


def tokenize(code: str) -> list[Token]:
    pattern = re.compile(r'\s*(\(|\)|"[^"]*"|[^\s()]+)\s*')
    tokens = pattern.findall(code)
    return [(match_token_type(token), token) for token in tokens]


def match_token_type(token: str) -> str:
    for token_type, regex in TOKENS.items():
        if re.fullmatch(regex, token):
            return token_type
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
