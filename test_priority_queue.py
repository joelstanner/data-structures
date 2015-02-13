# -*- coding: utf-8 -*-

import pytest
from priority_queue import PriorityQueue


test_priorityq_long = [10, 9, 8, 8, 7, 7, 7, 6, 5, 4, 3, 3, 3, 2, 1, 1, 1]
test_priorityq_short = []


@pytest.fixture(scope="function")
def test_priority_q_dups():
    test_pq = PriorityQueue()
    test_pq.insert(10, 'test1')
    test_pq.insert(10, 'test2')
    test_pq.insert(10, 'test3')
    test_pq.insert(1, 'test4')
    test_pq.insert(1, 'test5')
    test_pq.insert(2, 'test6')
    test_pq.insert(3, 'test7')
    test_pq.insert(4, 'test8')
    test_pq.insert(5, 'test9')
    test_pq.insert(5, 'test10')

    return test_pq


@pytest.fixture(scope="function")
def test_priority_q_no_dups():
    test_pq = PriorityQueue()
    test_pq.insert(1, 'test1')
    test_pq.insert(2, 'test2')
    test_pq.insert(3, 'test3')
    test_pq.insert(4, 'test4')
    test_pq.insert(5, 'test5')
    test_pq.insert(6, 'test6')
    test_pq.insert(7, 'test7')
    test_pq.insert(8, 'test8')
    test_pq.insert(9, 'test9')
    test_pq.insert(10, 'test10')

    return test_pq


def test_constructor():
    test_pq = PriorityQueue()
    assert test_pq._list == []
    assert test_pq.seniority == 0


def test_insert_value_is_inserted():
    test_pq = PriorityQueue()
    test_pq.insert(10, 'test1')


def test_insert_correctly_sorts_list_with_no_dups(test_priority_q_no_dups):
    expected_result = [10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
    result = []
    for item in test_priority_q_no_dups._list:
        result.append(item.priority)

    assert result == expected_result


def test_pop_empty(test_priority_q_dups):
    test_pq = PriorityQueue()
    with pytest.raises(IndexError) as error:
        test_pq.pop()
    assert 'The queue is empty' in str(error.value)


def test_pop_maintains_heap(test_priority_q_dups):
    assert test_priority_q_dups.pop().val == 'test1'
    assert test_priority_q_dups.pop().val == 'test2'
    assert test_priority_q_dups.pop().val == 'test3'
    assert test_priority_q_dups.pop().val == 'test9'
    assert test_priority_q_dups.pop().val == 'test10'


def test_pop_one_item_works():
    test_pq = PriorityQueue()
    test_pq.insert(10, "test")
    assert test_pq.pop().val == 'test'
    with pytest.raises(IndexError) as error:
        test_pq.pop()
    assert 'The queue is empty' in str(error.value)


def test_peek_returns_correct_value(test_priority_q_dups):
    result = test_priority_q_dups.peek()
    assert result == 'test1'


def test_peek_empty_raises_error():
    test_pq = PriorityQueue()
    with pytest.raises(IndexError) as error:
        test_pq.peek()
    assert 'The queue is empty' in str(error.value)
