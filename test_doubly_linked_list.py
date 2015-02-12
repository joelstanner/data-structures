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


def test_pop_list_with_only_one_item(test_dll):
    test_dll.pop()
    test_dll.pop()
    assert test_dll.pop() == "test3"


def test_pop_empty():
    test_dll = Dll()

    with pytest.raises(ValueError):
        test_dll.pop()


def test_pop_with_one_updates_tail():
    test_dll = Dll()
    test_dll.insert(3)
    test_dll.pop()

    with pytest.raises(ValueError):
        test_dll.shift()


def test_shift_returns_correct_value(test_dll):
    assert test_dll.shift() == 'test3'


def test_shift_updates_tail_correctly(test_dll):
    test_dll.shift()
    assert test_dll.tail.val == 'test1'


def test_shift_with_one_updates_head():
    test_dll = Dll()
    test_dll.insert(3)
    test_dll.shift()

    with pytest.raises(ValueError):
        test_dll.pop()


def test_search(test_dll):

    assert test_dll.search('test1').val == 'test1'


def test_remove_value(test_dll):
    test_dll.remove('test3')
    assert test_dll.search('test3') is None


def test_remove_value_not_in_list(test_dll):
    with pytest.raises(ValueError) as excinfo:
        test_dll.remove('test4')
    assert 'Value not found' in str(excinfo.value)


def test_remove_last_item():
    test_list = Dll()
    test_list.insert(5)
    test_list.remove(5)
    assert test_list.head is None and test_list.tail is None


def test_remove_updates_head(test_dll):
    test_dll.remove('test2')
    assert test_dll.pop() == 'test1'


def test_remove_updates_tail(test_dll):
    test_dll.remove('test3')
    assert test_dll.shift() == 'test1'


def test__str__returns_correct_output(test_dll):
    assert str(test_dll) == "('test2', 'test1', 'test3')"


def test__str__returns_single_output_if_only_one_item():
    test_list = Dll()
    test_list.insert('test')

    assert str(test_list) == "('test')"


def test_unicode():
    test_list = Dll()
    test_list.insert(u'ö')
    assert unicode(test_list) == u"('ö')"


def test_string():
    test_list = Dll()
    test_list.insert(u'éclaire')
    assert str(test_list) == "('\xc3\xa9claire')"
