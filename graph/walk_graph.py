from graph.exaple_data import nodeA, nodeC
from graph.g_node import GNode


def walk_graph(node: GNode) -> list[type[GNode]]:
    def drf(node: GNode):
        if node in result:
            return
        # there should not be any duplicates, since graph should be acyclic
        result.append(node)
        for child in node.children:
            drf(child)

    result = list()
    drf(node)
    return result


print("Node A", walk_graph(nodeA))
print("Node C", walk_graph(nodeC))
