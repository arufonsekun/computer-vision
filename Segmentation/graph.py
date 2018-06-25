class Graph:
    def __init__(self, vertex, edges):
        self.vertex = vertex
        self.edge = edges
        self.nodes = []
        self.nodeObjects = []


    def addNode(self):
        for _ in range(self.edge):
            e, v, w = map(int, input().split())
            if e not in self.nodes:
                node = Node()
                node.value = e
                self.nodes.append(e)
                node.connections.append(v)
                self.nodeObjects.append(node)
                
            if v not in self.nodes:
                node2 = Node()
                node2.value = v
                self.nodes.append(v)
                node.connections.append(e)
                self.nodeObjects.append(node2)


class Node:
    value = 0
    connections = []
    weight = []
    distance = 0

graph = Graph(3,3)
graph.addNode()
