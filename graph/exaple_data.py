"""
This file should be some pytest module (or unitest), but for demo it's going to work enough
"""
from graph.g_node import GNode

# Creating nodes
nodeA = GNode("A")
nodeB = GNode("B")
nodeC = GNode("C")
nodeD = GNode("D")
nodeE = GNode("E")
nodeF = GNode("F")
nodeG = GNode("G")
nodeH = GNode("H")
nodeI = GNode("I")
nodeJ = GNode("J")

nodeA.add_children([nodeB, nodeC, nodeD])
nodeB.add_children([nodeE, nodeF])
nodeC.add_children([nodeG, nodeH, nodeI])
nodeD.add_children([nodeJ])
