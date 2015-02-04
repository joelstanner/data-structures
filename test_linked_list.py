import pytest
from linked_list import LinkedList, Node



def test_value_inserts_at_the_head():
    test_list = LinkedList()
    test_list.insert('test')

    assert test_list.head.val == "test"


def test_pop():
    pass

def test_size():
    pass

def test_search():
    pass

def test_remove():
    pass


