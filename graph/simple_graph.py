class Graph(object):
    """Implements a graph data structure"""

    def __init__(self):
        self.graph_dict = {}

    def nodes(self):
        """return a list of all nodes in the graph"""
        return self.graph_dict.keys()

    def edges(self):
        """return a list of all edges in the graph"""

        return [(key, node) for key, value in
                self.graph_dict.iteritems() for node in value]

    def add_node(self, node):
        """add a new node 'n' to the graph"""
        self.graph_dict.setdefault(node, [])

    def add_edge(self, node_1, node_2):
        """add a new edge to the graph connecting 'n1' and 'n2', if either n1
        or n2 are not already present in the graph, they are added.
        """
        self.add_node(node_1)
        self.add_node(node_2)
        self.graph_dict[node_1].append(node_2)

    def del_node(self, node):
        """delete the node 'n' from the graph"""
        try:
            del self.graph_dict[node]
            for val_list in self.graph_dict.values():
                if node in val_list:
                    val_list.remove(node)
        except KeyError:
            raise KeyError("Node not found")

    def del_edge(self, node_1, node_2):
        """delete the edge connecting 'n1' and 'n2' from the graph"""
        try:
            self.graph_dict[node_1].remove(node_2)
        except KeyError:
            raise KeyError("First node not found")
        except ValueError:
            raise ValueError("Edge not found")

    def has_node(self, node):
        """True if node 'n' is contained in the graph, False if not"""
        return node in self.graph_dict

    def neighbors(self, node):
        """return the list of all nodes connected to 'n' by edges"""
        try:
            return self.graph_dict[node]
        except KeyError:
            raise KeyError("Node not found")

    def adjacent(self, node_1, node_2):
        """return True if there is an edge connecting n1 and n2, False if not
        """
        if not self.has_node(node_2):
            raise KeyError("Second node not found")
        try:
            return node_2 in self.graph_dict[node_1]
        except KeyError:
            raise KeyError("First node not found")
