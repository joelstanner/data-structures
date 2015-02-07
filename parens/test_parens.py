from parens import Parens

def test_equal_unmatched():
    assert Parens(")(") == -1

def test_equal_parens():
    assert Parens("()") == 0


def test_open():
    assert Parens("(") == 1


def test_two_open():
    assert Parens("((") == 1


def test_broken():
    assert Parens(")") == -1


def test_combo():
    assert Parens(")(()))(") == -1


def test_combo_2():
    assert Parens("(()") == 1

def test_example():
    assert Parens(')))(((') == -1
