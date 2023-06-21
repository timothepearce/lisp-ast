from main import *


def test_tokenize_string():
    code = '(print "Hello Lisp!")'
    tokens = [
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_KEYWORD, "print"),
        (TOKEN_STRING, '"Hello Lisp!"'),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
    ]
    ast = ["print", "Hello Lisp!"]

    assert tokenize(code) == tokens
    assert build_ast(tokens) == ast


def test_tokenize_number():
    code = "(first (list 1 (+ 2 3) 9))"
    tokens = [
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_KEYWORD, "first"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_KEYWORD, "list"),
        (TOKEN_NUMBER, "1"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_OPERATOR, "+"),
        (TOKEN_NUMBER, "2"),
        (TOKEN_NUMBER, "3"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_NUMBER, "9"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
    ]
    ast = ["first", ["list", 1, ["+", 2, 3], 9]]

    assert tokenize(code) == tokens
    assert build_ast(tokens) == ast


def test_tokenize_anonymous_function():
    code = "(lambda (x) (* x x))"
    tokens = [
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_KEYWORD, "lambda"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_IDENTIFIER, "x"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_OPERATOR, "*"),
        (TOKEN_IDENTIFIER, "x"),
        (TOKEN_IDENTIFIER, "x"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
    ]
    ast = ["lambda", ["x"], ["*", "x", "x"]]

    assert tokenize(code) == tokens
    assert build_ast(tokens) == ast


def test_tokenize_factorial_function():
    code = """
    (defun factorial (n)
        (if (<= n 1)
            1
            (* n (factorial (- n 1)))))
    """
    tokens = [
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_KEYWORD, "defun"),
        (TOKEN_IDENTIFIER, "factorial"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_IDENTIFIER, "n"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_KEYWORD, "if"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_OPERATOR, "<="),
        (TOKEN_IDENTIFIER, "n"),
        (TOKEN_NUMBER, "1"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_NUMBER, "1"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_OPERATOR, "*"),
        (TOKEN_IDENTIFIER, "n"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_IDENTIFIER, "factorial"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_OPERATOR, "-"),
        (TOKEN_IDENTIFIER, "n"),
        (TOKEN_NUMBER, "1"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
    ]
    ast = ["defun", "factorial", ["n"], ["if", ["<=", "n", 1], 1, ["*", "n", ["factorial", ["-", "n", 1]]]]]

    assert tokenize(code) == tokens
    assert build_ast(tokens) == ast
