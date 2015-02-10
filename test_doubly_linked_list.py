# -*- coding: utf-8 -*-

from doubly_linked_list import DoublyLinkedList as Dll
import pytest


@pytest.fixture(scope="function")
def test_dll():
    test_dll = Dll()
    test_dll.insert('test1')
    test_dll.insert('test2')
    test_dll.append('test3')

    return test_dll


def test_constructor():
    test_dll = Dll()

    assert test_dll.head is None
    assert test_dll.tail is None


def test_value_inserts_at_the_head(test_dll):

    assert test_dll.head.val == "test2"


def test_append(test_dll):
    assert test_dll.tail.val == 'test3'


def test_pop_returns_correct_head(test_dll):

    assert test_dll.pop() == "test2"


def test_pop_updates_head(test_dll):

    test_dll.pop()

    assert test_dll.head.val == "test1"


def test_pop_empty():
    test_dll = Dll()

    with pytest.raises(ValueError):
        test_dll.pop()


def test_shift_returns_correct_value(test_dll):
    assert test_dll.shift() == 'test3'


def test_shift_updates_tail_correctly(test_dll):
    test_dll.shift()
    assert test_dll.tail.val == 'test1'


def test_search(test_dll):

    assert test_dll.search('test1').val == 'test1'


def test_remove_unique_node(test_dll):
    the_node = test_dll.search('test2')
    test_dll.remove('test2')
    pointer = test_dll.head

    while pointer:
        assert pointer is not the_node
        pointer = pointer.next



#def test__str__returns_correct_output():
#    test_list = LinkedList()
#    test_list.insert('test2')
#    test_list.insert(1)
#    test_list.insert('test3')
#    test_list.insert(2)
#
#    assert str(test_list) == "(2, 'test3', 1, 'test2')"
#
#
#def test__str__returns_single_output_if_only_one_item():
#    test_list = LinkedList()
#    test_list.insert('test')
#
#    assert str(test_list) == "('test')"
#
#
#def test_unicode():
#    test_list = LinkedList()
#    test_list.insert(u'ö')
#    assert unicode(test_list) == u"('ö')"
#
#
#def test_string():
#    test_list = LinkedList()
#    test_list.insert(u'éclaire')
#    assert str(test_list) == "('\xc3\xa9claire')"
