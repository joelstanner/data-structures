from __future__ import unicode_literals
from linked_list import LinkedList


def test_constructor():
    test_list = LinkedList()

    assert test_list.head is None

def test_value_inserts_at_the_head():
    test_list = LinkedList()
    test_list.insert('test')

    assert test_list.head.val == "test"


def test_pop_returns_correct_head():
    test_list = LinkedList()
    test_list.insert('test')

    assert test_list.pop() == "test"

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


def test_remove_unique_node():
    test_list = LinkedList()
    test_list.insert('test')
    test_list.insert('test2')
    test_list.insert('tester')

    the_node = test_list.search('tester')

    test_list.insert('tester')

    test_list.remove(the_node)

    pointer = test_list.head


    assert pointer is not the_node

    while pointer.next:
        assert pointer.next is not the_node
        pointer = pointer.next




def test__str__returns_correct_output():
    test_list = LinkedList()
    test_list.insert('test2')
    test_list.insert(1)
    test_list.insert('test3')
    test_list.insert(2)

    assert str(test_list) == "(2, 'test3', 1, 'test2')"

def test__str__returns_single_output_if_only_one_item():
    test_list = LinkedList()
    test_list.insert('test')

    assert str(test_list) == "('test')"
