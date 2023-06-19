from main import tokenize, lisp_to_ast


def test_tokenize_string():
    code = "(print \"Hello Lisp!\")"
    assert tokenize(code) == ["(", "print", "\"Hello Lisp!\"", ")"]


def test_tokenize_integer():
    code = "(first (list 1 (+ 2 3) 9))"
    assert tokenize(code) == ['(', 'first', '(', 'list', '1', '(', '+', '2', '3', ')', '9', ')', ')']
