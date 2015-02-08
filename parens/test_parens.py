from parens import Parens


def test_equal_unmatched():
    assert Parens(u")(") == -1


def test_equal_parens():
    assert Parens(u"()") == 0


def test_open():
    assert Parens(u"(") == 1


def test_two_open():
    assert Parens(u"((") == 1


def test_broken():
    assert Parens(u")") == -1


def test_many_equal():
    assert Parens(u"(()(()))") == 0


def test_combo():
    assert Parens(u")(()))(") == -1


def test_combo_2():
    assert Parens(u"(()") == 1


def test_example():
    assert Parens(u')))(((') == -1
