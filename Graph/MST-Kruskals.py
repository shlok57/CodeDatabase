def Kruskals(graph):

    parent = [i for i in range(len(graph))]

    def findParent(node):
        while node != parent[node]:
            node = parent[node]
        return node

    def union(node1, node2):
        a = findParent(node1)
        b = findParent(node2)
        parent[a] = b

    minCost = 0
    edgeCount = 0
    while edgeCount < len(graph) - 1:
        m = 99999
        a = -1
        b = -1

        for i in range(len(graph)):
            for j in range(len(graph)):
                if findParent(i) != findParent(j) and graph[i][j] and m > graph[i][j]:
                    m = graph[i][j]
                    a = i
                    b = j
        union(a, b)
        print("Edge ", a, " ", b, " ", m)
        minCost += m
        edgeCount += 1
    print("Result ", minCost)


Kruskals([
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
])
