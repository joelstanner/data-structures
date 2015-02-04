import pytest
import pdb
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


def test_pop_empty():
    test_list = LinkedList()

    assert test_list.pop() is None


def test_size():
    test_list = LinkedList()
    test_list.insert('test')
    test_list.insert('test2')
    test_list.insert('test')
    test_list.insert('test2')

    assert test_list.size() == 4


def test_size_one():
    test_list = LinkedList()
    test_list.insert('test')

    assert test_list.size() == 1


def test_size_zero():
    test_list = LinkedList()

    assert test_list.size() == 0


def test_size_after_pop():
    test_list = LinkedList()
    test_list.insert('test')
    test_list.insert('test2')
    test_list.insert('test')
    test_list.insert('test2')
    test_list.pop()

    assert test_list.size() == 3


def test_search_first():
    test_list = LinkedList()
    test_list.insert('test')
    test_list.insert('test2')
    test_list.insert('test3')

    assert test_list.search('test3').val == 'test3'


def test_search_last():
    test_list = LinkedList()
    test_list.insert('test')
    test_list.insert('test2')
    test_list.insert('test3')

    assert test_list.search('test').val == 'test'


def test_search_none():
    test_list = LinkedList()
    test_list.insert('test')
    test_list.insert('test2')
    test_list.insert('test3')

    assert test_list.search('test4') is None


def test_remove_removes_node():
    test_list = LinkedList()
    test_list.insert('test')
    test_list.insert('test2')
    test_list.insert('tester')
    test_node = test_list.head
    test_node_id = id(test_node)
    test_list.insert('test3')


    #pdb.set_trace()
    #print(test_node_id)

    test_list.remove(test_node)
    
    assert test_list.search('tester') is None



