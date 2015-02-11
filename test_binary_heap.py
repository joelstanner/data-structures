# -*- coding: utf-8 -*-

import pytest
from binary_heap import Binaryheap as B_heap

test_array = [123, 3, 32, 646, 7, 235]

@pytest.fixture(scope="function")
def test_heap():
    testing_heap


def test_constructor():
    test = B_heap()
    assert test._list is None


def test_push_value_is_inserted():
    test_heap = B_heap()
    test_heap.push(100)

    assert test_heap._list[0] == 100

def test_push_correctly_sorts():
    
