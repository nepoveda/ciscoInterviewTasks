from typing import Self


class GNode:
    def __init__(self, name: str, children: list | None = None):
        self.name = name
        self.children = children if children is not None else []

    def get_name(self) -> str:
        return self.name

    # I know this wasn't in task interface, but it's going to be handy
    def add_children(self, nodes: list[type[Self]]) -> None:
        self.children.extend(nodes)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
