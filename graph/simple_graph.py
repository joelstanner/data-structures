class Graph(object):
    """Implements a graph data structure"""

    def __init__(self):
        self.graph_dict = {}

    def nodes(self):
        return self.graph_dict.keys()

    def edges(self):
        edge_list = []
        for key, value in self.graph_dict.items():
            for item in value:
                edge_list.append((key, item))
        return edge_list

        # return [(key, value) for key, value in self.graph_dict.items()]

    def add_node(self, node):
        self.graph_dict[node] = []

    def add_edge(self, node_1, node_2):
        self.graph_dict[node_1].append(node_2)

    def del_node(self, node):
        del self.graph_dict[node]
        for val_list in self.graph_dict.values():
            if node in val_list:
                val_list.remove(node)

    def del_edge(self, node_1, node_2):
        pass

    def has_node(self, node):
        pass

    def neighbors(self, node):
        pass

    def adjacent(self, node_1, node_2):
        pass
