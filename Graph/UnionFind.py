from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, start, end):
        self.graph[start].append(end)

    def find_parent(self, parent, node):
        while parent[node] != -1:
            return self.find_parent(parent, parent[node])
        return node

    def union(self, parent, x, y):
        xp = self.find_parent(parent, x)
        yp = self.find_parent(parent, y)
        parent[xp] = yp
        pass

    def isCyclic(self):
        parent = [-1]*self.V
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)
        return False


if __name__ == "__main__":
    G = Graph(3)
    G.addEdge(0, 1)
    G.addEdge(1, 2)
    G.addEdge(2, 0)
    print(G.isCyclic())

    G = Graph(4)
    G.addEdge(0, 1)
    G.addEdge(1, 2)
    G.addEdge(2, 3)
    print(G.isCyclic())
    pass
