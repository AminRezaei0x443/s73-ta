from .node import Node


class Network:
    ID_COUNTER = 0
    nodes: dict[int, Node]
    trees: list[Node]

    def __init__(self):
        self.nodes = {}
        self.trees = []

    def add_node(self, capacity: int) -> int:
        n = Node(Network.ID_COUNTER, capacity)
        Network.ID_COUNTER += 1
        self.nodes[n.id] = n
        self._add_to_topology(n)
        return n.id

    def _add_to_topology(self, node: Node) -> None:
        for t in self.trees:
            slot = t.find_slot()
            if slot:
                slot.add_child(node)
                return
        self.trees.append(node)

    def remove_node(self, id: int) -> bool:
        pass

    def topology(self, format="text") -> str:
        pass
