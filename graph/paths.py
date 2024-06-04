from graph.exaple_data import nodeA, nodeC
from graph.g_node import GNode


def paths(node: GNode) -> list[list[GNode]]:
    def dsf(current_node: GNode, current_path: list, all_paths: list):
        current_path.append(current_node)
        # if it's leaf node
        if not current_node.children:
            all_paths.append(current_path)
        else:
            for child in current_node.children:
                # call it with copy of current path
                dsf(child, current_path.copy(), all_paths)

    result = []
    dsf(node, [], result)
    return result


print("Paths A", paths(nodeA))
print("Paths C", paths(nodeC))
