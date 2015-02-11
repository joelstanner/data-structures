# -*- coding: utf-8 -*-

import pytest
from binary_heap import BinaryHeap as B_heap

TEST_ARRAY = [123, 3, 32, 646, 7, 235]


@pytest.fixture(scope="function")
def test_heap():
    test_heap = B_heap()
    test_heap.push(7)
    test_heap.push(8)
    test_heap.push(9)
    test_heap.push(3)

    return test_heap


def test_constructor():
    test = B_heap()
    assert test._list == []


def test_constructor_with_iterable():
    test = B_heap(TEST_ARRAY)
    assert test._list == [646, 123, 235, 3, 7, 32]


def test_push_value_is_inserted():
    test_heap = B_heap()
    test_heap.push(100)

    assert test_heap._list[0] == 100


def test_push_correctly_sorts(test_heap):
    assert test_heap._list == [9, 7, 8, 3]
