import pytest
from linked_list import LinkedList, Node



def test_value_inserts_at_the_head():
    test_list = LinkedList()
    test_list.insert('test')

    assert test_list.head.val == "test"


def test_pop_returns_correct_head():
    test_list = LinkedList()
    test_list.insert('test')

    assert test_list.pop().val == "test"

def test_pop_updates_head():
    test_list = LinkedList()
    test_list.insert('test')
    test_list.insert('test2')

    test_list.pop()

    assert test_list.head.val == "test"



def test_size():
    pass

def test_search():
    pass

def test_remove():
    pass


