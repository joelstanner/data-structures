# -*- coding: utf-8 -*-

from stack import Stack, Item

def test_constructor():
    test_stack = Stack()

    assert test_stack.top is None

def test_push_accepts_item():
    item = Item("test")
    test_stack = Stack()
    test_stack.push(item)
    
    assert test_stack.top == item
