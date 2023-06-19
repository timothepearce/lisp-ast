from main import *


def test_tokenize_string():
    code = '(print "Hello Lisp!")'
    assert tokenize(code) == [
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_SYMBOL, "print"),
        (TOKEN_STRING, '"Hello Lisp!"'),
        (TOKEN_RIGHT_PARENTHESIS, ")"),
    ]


def test_tokenize_number():
    code = "(first (list 1 (+ 2 3) 9))"
    assert tokenize(code) == [
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_SYMBOL, "first"),
        (TOKEN_LEFT_PARENTHESIS, "("),
        (TOKEN_SYMBOL, "list"),
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
