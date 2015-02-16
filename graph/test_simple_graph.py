import pytest
from simple_graph import Graph


@pytest.fixture(scope="function")
def test_graph():
    test_graph = Graph()
    test_graph.add_node(5)
    test_graph.add_node(42)
    test_graph.add_node("test")
    test_graph.add_edge(5, 42)
    test_graph.add_edge(42, "test")
    test_graph.add_edge("test", 5)

    return test_graph


def test_constructor():
    test = Graph()
    assert test.graph_dict == {}


def test_add_node():
    test = Graph()
    test.add_node(5)
    assert 5 in test.graph_dict


def test_add_edge():
    test = Graph()
    test.add_node(5)
    test.add_node(42)
    test.add_edge(5, 42)

    assert test.graph_dict[5] == 42


def test_get_nodes(test_graph):
    assert test_graph.nodes() == [5, 42, "test"]


def test_get_edges(test_graph):
    assert test_graph.edges() == [(5, 42), (42, "test"), ("test", 5)]
