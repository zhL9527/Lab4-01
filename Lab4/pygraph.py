from collections import defaultdict
from typing import List, Tuple, Set, Dict, Optional


class Graph:
    def __init__(self, edges: List[Tuple] = [], directed: bool = True):
        self.directed = directed
        self.adjacency: Dict = defaultdict(dict)

        nodes = set()
        for u, v in edges:
            nodes.update([u, v])
        for node in nodes:
            self.adjacency[node] = {"in": set(), "out": set()}

        for u, v in edges:
            self._add_edge(u, v)

    def has_node(self, node) -> bool:
        return node in self.adjacency

    def has_edge(self, edge: Tuple) -> bool:
        u, v = edge
        if not self.has_node(u) or not self.has_node(v):
            return False
        return v in self.adjacency[u]["out"]

    def add_node(self, node):
        if not self.has_node(node):
            self.adjacency[node] = {"in": set(), "out": set()}

    def add_edge(self, edge: Tuple):
        u, v = edge
        if not self.has_node(u):
            self.add_node(u)
        if not self.has_node(v):
            self.add_node(v)
        self._add_edge(u, v)

    def _add_edge(self, u, v):
        self.adjacency[u]["out"].add(v)
        self.adjacency[v]["in"].add(u)

        if not self.directed:
            self.adjacency[v]["out"].add(u)
            self.adjacency[u]["in"].add(v)

    def remove_node(self, node):
        if not self.has_node(node):
            raise ValueError(f"Node {node} not in graph")

        for neighbor in list(self.adjacency[node]["in"]):
            self.adjacency[neighbor]["out"].discard(node)
            if not self.directed:
                self.adjacency[neighbor]["in"].discard(node)

        for neighbor in list(self.adjacency[node]["out"]):
            self.adjacency[neighbor]["in"].discard(node)
            if not self.directed:
                self.adjacency[neighbor]["out"].discard(node)

        del self.adjacency[node]

    def remove_edge(self, edge: Tuple):
        u, v = edge
        if not self.has_edge(edge):
            raise ValueError(f"Edge {edge} not in graph")

        self.adjacency[u]["out"].discard(v)
        self.adjacency[v]["in"].discard(u)

        if not self.directed:
            self.adjacency[v]["out"].discard(u)
            self.adjacency[u]["in"].discard(v)

    def indegree(self, node) -> int:
        if not self.has_node(node):
            raise ValueError(f"Node {node} not in graph")
        return len(self.adjacency[node]["in"])

    def outdegree(self, node) -> int:
        if not self.has_node(node):
            raise ValueError(f"Node {node} not in graph")
        return len(self.adjacency[node]["out"])

    def __str__(self):
        return f"Graph(directed={self.directed}, adjacency={dict(self.adjacency)})"

    def __repr__(self):
        return str(self)
