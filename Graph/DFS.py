from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addedge(self,start,end):
        self.graph[start].append(end)
        
    def DFS(self,start):
        
        visited = []
        queue = []
        
        queue.append(start)
        visited.append(start)
        
        while queue:
            # print node
            node = queue.pop()
            print node
            for neigh in self.graph[node]:
                if neigh not in visited:
                    queue.append(neigh)
                    visited.append(neigh)
                    
a = Graph()
a.addedge(0,1)
a.addedge(0,2)
a.addedge(0,3)
a.addedge(1,5)
a.addedge(2,4)
a.addedge(3,4)
a.addedge(3,5)
a.addedge(4,5)
a.addedge(5,0)

a.DFS(0)