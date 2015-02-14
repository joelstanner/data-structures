# -*- coding: utf-8 -*-

import pytest
from queue import Queue


@pytest.fixture(scope="function")
def test_queue():
    test = Queue()
    test.enqueue(3)
    test.enqueue("test")
    return test


def test_constructor():
    test = Queue()
    assert test.front is None
    assert test.back is None


def test_enqueue(test_queue):
    assert test_queue.front.val == 3


def test_enqueue_none():
    test = Queue()
    test.enqueue(None)
    assert test.front.val is None


def test_dequeue(test_queue):
    assert test_queue.dequeue() == 3
    assert test_queue.dequeue() == "test"


def test_dequeue_with_one():
    test_queue = Queue()
    test_queue.enqueue(3)
    test_queue.dequeue()

    assert test_queue.front is None
    assert test_queue.back is None


def test_dequeue_empty(test_queue):
    test_queue.dequeue()
    test_queue.dequeue()

    with pytest.raises(AttributeError) as excinfo:
        test_queue.dequeue()

    assert 'The queue is empty' in str(excinfo.value)


def test_size(test_queue):
    assert test_queue.size() == 2
    test_queue.enqueue(42)
    assert test_queue.size() == 3


def test_size_zero():
    test = Queue()
    assert test.size() == 0
