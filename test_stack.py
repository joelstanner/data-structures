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

def test_push_places_item_on_top():
    test_stack = Stack()
    item = Item("test")
    item2 = Item(42)
    test_stack.push(item)
    test_stack.push(item2)
    
    assert test_stack.top == item2
    
