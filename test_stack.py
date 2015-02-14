# -*- coding: utf-8 -*-

import pytest
from stack import Stack


def test_constructor():
    test_stack = Stack()

    assert test_stack.top is None


def test_push_accepts_item():
    test_stack = Stack()
    test_stack.push((1, 2, 3))

    assert test_stack.top.data == (1, 2, 3)


def test_push_places_item_on_top():
    test_stack = Stack()
    test_stack.push("test")
    test_stack.push(42)

    assert test_stack.top.data == 42


def test_push_empty():
    test_stack = Stack()

    with pytest.raises(TypeError) as excinfo:
        test_stack.push()

    assert 'push() takes exactly 2 arguments (1 given)' in str(excinfo.value)


def test_pop():
    test_stack = Stack()
    test_stack.push("test")
    test_stack.push(42)

    assert test_stack.pop() == 42
    assert test_stack.top.data == "test"


def test_pop_empty():
    test_stack = Stack()

    with pytest.raises(ValueError) as excinfo:
        test_stack.pop()

    assert 'The stack is empty' in str(excinfo.value)
