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


def test_add_edge_first_node_new():
    test = Graph()
    test.add_node(55)
    test.add_edge("test", 55)
    assert "test" in test.graph_dict
    assert 55 in test.graph_dict["test"]


def test_add_edge_second_node_new():
    test = Graph()
    test.add_node(55)
    test.add_edge(55, "test")
    assert "test" in test.graph_dict
    assert "test" in test.graph_dict[55]


def test_nodes(test_graph):
    assert test_graph.nodes() == ["test", 42, 5]


def test_edges(test_graph):
    assert test_graph.edges() == [("test", 5), (42, "test"), (5, 42)]


def test_del_node(test_graph):
    test_graph.add_edge("test", "purple")
    assert 42 in test_graph.nodes()
    test_graph.del_node(42)
    assert 42 not in test_graph.nodes()
    for edge_list in test_graph.graph_dict.values():
        assert 42 not in edge_list


def test_del_node_not_found(test_graph):
    with pytest.raises(KeyError) as e:
        test_graph.del_node("test2")
    assert "Node not found" in str(e.value)


def test_del_edge(test_graph):
    test_graph.del_edge(5, 42)
    assert 42 not in test_graph.graph_dict[5]


def test_del_edge_not_found(test_graph):
    with pytest.raises(ValueError) as e:
        test_graph.del_edge(5, "test")
    assert "Edge not found" in str(e.value)


def test_del_edge_node_not_found(test_graph):
    with pytest.raises(KeyError) as e:
        test_graph.del_edge(8, "test")
    assert "First node not found" in str(e.value)


def test_has_node_true(test_graph):
    assert test_graph.has_node(5)


def test_has_node_false(test_graph):
    assert not test_graph.has_node(6)


def test_neighbors(test_graph):
    assert test_graph.neighbors(5) == [42]


def test_neighbors_not_found(test_graph):
    with pytest.raises(KeyError) as e:
        test_graph.neighbors(6)
    assert 'Node not found' in str(e.value)


def test_adjacent(test_graph):
    assert test_graph.adjacent(42, "test")


def test_adjacent_first_node_not_found(test_graph):
    with pytest.raises(KeyError) as e:
        test_graph.adjacent("test2", 42)
    assert 'First node not found' in str(e.value)


def test_adjacent_second_node_not_found(test_graph):
    with pytest.raises(KeyError) as e:
        test_graph.adjacent("test", 47)
    assert 'Second node not found' in str(e.value)
