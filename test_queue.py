# -*- coding: utf-8 -*-

import pytest
from queue import Queue


@pytest.fixture(scope="function")
def test_queue():
    test = Queue()
    test.enqueue(3)
    test.enqueue("test")
    return test


def test_enqueue(test_queue):
    assert test_queue.front.val == 3


def test_enqueue_none():
    test = Queue()
    test.enqueue(None)
    assert test.front.val is None


def test_dequeue(test_queue):
    test_queue.enqueue(None)
    assert test_queue.dequeue() == 3
