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

    assert 42 in test.graph_dict[5]


def test_get_nodes(test_graph):
    assert test_graph.nodes() == ["test", 42, 5]


def test_get_edges(test_graph):
    assert test_graph.edges() == [("test", 5), (42, "test"), (5, 42)]


def test_del_node(test_graph):
    assert 42 in test_graph.nodes()
    test_graph.del_node(42)
    assert 42 not in test_graph.nodes()
    for edge_list in test_graph.graph_dict.values():
        assert 42 not in edge_list
