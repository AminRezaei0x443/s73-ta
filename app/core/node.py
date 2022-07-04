from typing import Union


class Node:
    id: int
    capacity: int
    children: list["Node"]

    def __init__(self, id: int, cap: int):
        self.id = id
        self.capacity = cap
        self.children = []

    def has_capacity(self) -> bool:
        return len(self.children) < self.capacity

    def add_child(self, node: "Node") -> None:
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
