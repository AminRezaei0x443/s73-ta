from typing import Union


class Node:
    id: int
    capacity: int
    children: list["Node"]
    parent: Union["Node", None]

    def __init__(self, id: int, cap: int):
        self.id = id
        self.capacity = cap
        self.children = []
        self.parent = None

    def has_capacity(self) -> bool:
        return len(self.children) < self.capacity

    def add_child(self, node: "Node") -> None:
        node.parent = self
        self.children.append(node)

    def find_slot(self) -> Union["Node", None]:
        if self.has_capacity():
            return self
        else:
            for child in self.children:
                slot = child.find_slot()
                if slot:
                    return slot
        return None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "capacity": self.capacity,
            "children": list(map(lambda x: x.to_dict(), self.children))
        }

    def clear_children(self):
        self.children.clear()