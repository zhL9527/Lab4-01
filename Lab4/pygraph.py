from typing import Tuple, Union, Iterable
Node = Union[str, int]
Edge = Tuple[Node, Node]



class Graph(object):
    """Graph data structure, undirected by default."""
    def __init__(self, edges: Iterable[Edge] = [], directed: bool = False):
        self._directed = directed
        self._adjacency: Dict[Node, Set[Node]] = {}
        for node1, node2 in edges:
            self.add_edge((node1, node2))


def has_node(self, node: Node):
            """Whether a node is in graph"""
            return node in self._adjacency
    def has_edge(self, edge: Edge):
        node1, node2 = edge
        if not (self.has_node(node1) and self.has_node(node2)):
            return False

        return node2 in self._adjacency[node1] or (
                not self._directed and node1 in self._adjacency[node2]
        )



     """Whether an edge is in graph"""

    def add_node(self, node: Node):
       """Add a node"""
       if node not in self._adjacency:
           self._adjacency[node] = set()



    def add_edge(self, edge: Edge):
        node1, node2 = edge
        self.add_node(node1)
        self.add_node(node2)
        self._adjacency[node1].add(node2)
        if not self._directed:  # 无向图需对称添加
            self._adjacency[node2].add(node1)

        """Add an edge (node1, node2). For directed graph, node1 -> node2"""

    def remove_node(self, node: Node):
     """Remove all references to node"""
     if node in self._adjacency:
         del self._adjacency[node]
         # 遍历其他节点的邻接表，移除对该节点的引用
     for adjacent in self._adjacency.values():
         if node in adjacent:
             adjacent.remove(node)


    def remove_edge(self, edge: Edge):
        node1, node2 = edge
        if node1 in self._adjacency and node2 in self._adjacency[node1]:
            self._adjacency[node1].remove(node2)
        # 无向图需同步删除反向边
        if not self._directed and node2 in self._adjacency and node1 in self._adjacency[node2]:
            self._adjacency[node2].remove(node1)

        """Remove an edge from graph"""
           r
    def indegree(self, node: Node) -> int:
      """Compute indegree for a node"""
      if not self.has_node(node):
          return 0
      if not self._directed:  # 无向图的入度=出度=度数
          return len(self._adjacency[node])
          # 有向图：统计有多少边指向该节点
      return sum(1 for adjacent in self._adjacency.values() if node in adjacent)


    def outdegree(self, node: Node) -> int:
        return len(self._adjacency[node]) if self.has_node(node) else 0

        """Compute outdegree for a node"""

        
    def __str__(self):
        edges = []
        for node, neighbors in self._adjacency.items():
            for neighbor in neighbors:
                if self._directed or (neighbor, node) not in edges:  # 避免无向图重复打印
                    edge_str = f"{node} -> {neighbor}" if self._directed else f"{node} -- {neighbor}"
                    edges.append(edge_str)
        return "\n".join(edges) if edges else "空图"

    def __repr__(self):
        return f"Graph(有向={self._directed}, 邻接表={self._adjacency})"

