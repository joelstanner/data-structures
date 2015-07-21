from collections import OrderedDict
from queue import Queue
from Queue import PriorityQueue


W_DEFAULT = 1


class Graph(object):
    """Implements a graph data structure"""

    def __init__(self):
        self.graph_dict = {}

    def nodes(self):
        """return a list of all nodes in the graph"""
        return self.graph_dict.keys()

    def edges(self):
        """return a list of all edges in the graph"""

        return [(key, node, weight) for key, edge_dict in
                self.graph_dict.iteritems() for node, weight in edge_dict.items()]

    def add_node(self, node):
        """add a new node 'n' to the graph"""
        self.graph_dict.setdefault(node, OrderedDict())

    def add_edge(self, node_1, node_2, weight=W_DEFAULT):
        """add a new edge to the graph connecting 'n1' and 'n2', if either n1
        or n2 are not already present in the graph, they are added.
        """

        try:
            self.add_node(node_2)
            self.graph_dict[node_1][node_2] = weight
        except KeyError:
            self.add_node(node_1)
            self.graph_dict[node_1][node_2] = weight

    def del_node(self, node):
        """delete the node 'n' from the graph"""
        try:
            del self.graph_dict[node]
            for val_dict in self.graph_dict.values():
                if node in val_dict:
                    del val_dict[node]
        except KeyError:
            raise KeyError("Node not found")

    def del_edge(self, node_1, node_2):
        """delete the edge connecting 'n1' and 'n2' from the graph"""
        try:
            del self.graph_dict[node_1][node_2]
        except KeyError:
            raise KeyError("Edge not found")

    def has_node(self, node):
        """True if node 'n' is contained in the graph, False if not"""
        return node in self.graph_dict

    def neighbors(self, node):
        """return the list of all nodes connected to 'n' by edges"""
        try:
            return self.graph_dict[node].keys()
        except KeyError:
            raise KeyError("Node not found")

    def adjacent(self, node_1, node_2):
        """return True if there is an edge connecting n1 and n2, False if not
        """
        try:
            return node_2 in self.graph_dict[node_1]
        except KeyError:
            raise KeyError("First node not found")

    def depth_first_traversal(self, start):
        """Perform a full depth-first traversal of the graph beginning at start.
        Return the full visited path when traversal is complete.
        """
        try:
            explored = OrderedDict()
            return self._depth_first_traversal(start, explored)
        except KeyError:
            raise KeyError("Node does not exist")

    def _depth_first_traversal(self, start, explored):
        """Helper function for depth_first_traversal for recursion"""
        explored.setdefault(start, 1)

        for child in self.graph_dict[start]:
            if child not in explored:
                self._depth_first_traversal(child, explored)

        return explored.keys()

    def breadth_first_traversal(self, start):
        """Perform a full breadth-first traversal of the graph, beginning at
        start. Return the full visited path when traversal is complete.
        """
        try:
            explored = OrderedDict()
            queue = Queue()
            explored.setdefault(start, 1)

            queue.enqueue(start)

            while queue.size():
                node = queue.dequeue()

                for child in self.graph_dict[node]:
                    if child not in explored:
                        explored.setdefault(child, 1)
                        queue.enqueue(child)

            return explored.keys()
        except KeyError:
            raise KeyError("Node does not exist")

    def dijkstra_shortest(self, start, end):
        """Implementation of Dijkstra's shortest path algorithm, returns a list
        of shortest path from start to end"""
        if start is end:
            return [start]
        distance = {start: 0}
        previous_node = {}
        pqueue = PriorityQueue()
        for node in self.nodes():
            if node is not start:
                distance[node] = float('inf')
                previous_node['node'] = None
            pqueue.put((distance[node], node))  # (priority, data)

        while pqueue:
            current = pqueue.get()[1]
            if current == end:
                break
            for neighbor in self.neighbors(current):
                alt = distance[current] + self.graph_dict[current][neighbor]
                if alt < distance[neighbor]:
                    distance[neighbor] = alt
                    previous_node[neighbor] = current
                    pqueue.put((distance[neighbor], neighbor))

        path = []
        while end is not start:
            path.append(end)
            try:
                end = previous_node[end]
            except KeyError:
                return "No Path Found"
        path.append(start)
        path.reverse()
        return path

    def bellman_ford_shortest(self, start, end):
        """Implementation of Bellman-Ford's shortest path algorithm, returns a
        list of shortest path from start to end"""
        if start is end:
            return [start]
        distance = {start: 0}
        previous_node = {}
        # Step 1: initialize graph
        for node in self.nodes():
            if node is not start:
                distance[node] = float('inf')
                previous_node[node] = None

        # Step 2: relax edges repeatedly
        for i in range(1, len(self.nodes()) - 1):
            for edge in self.edges():
                if distance[edge[0]] + edge[2] < distance[edge[1]]:
                    distance[edge[1]] = distance[edge[0]] + edge[2]
                    previous_node[edge[1]] = edge[0]

        # Step 3: check for negative-weight cycles
        for edge in self.edges():
            if distance[edge[0]] + edge[2] < distance[edge[1]]:
                raise Exception("Graph contains a negative-weight cycle")

        path = []
        while end is not start:
            path.append(end)
            try:
                end = previous_node[end]
            except KeyError:
                return "No Path Found"
        path.append(start)
        path.reverse()
        return path
