from main import *


def test_tokenize_string():
    code = '(print "Hello Lisp!")'
    assert tokenize(code) == [
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_KEYWORD, "print"),
        (TOKEN_STRING, '"Hello Lisp!"'),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
    ]


def test_tokenize_number():
    code = "(first (list 1 (+ 2 3) 9))"
    assert tokenize(code) == [
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_KEYWORD, "first"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_KEYWORD, "list"),
        (TOKEN_NUMBER, "1"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_SYMBOL, "+"),
        (TOKEN_NUMBER, "2"),
        (TOKEN_NUMBER, "3"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_NUMBER, "9"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
    ]


def test_tokenize_anonymous_function():
    code = "(lambda (x) (* x x))"
    assert tokenize(code) == [
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_KEYWORD, "lambda"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_SYMBOL, "x"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_SYMBOL, "*"),
        (TOKEN_SYMBOL, "x"),
        (TOKEN_SYMBOL, "x"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
    ]
