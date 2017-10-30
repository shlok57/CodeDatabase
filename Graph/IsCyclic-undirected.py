from collections import defaultdict

class Graph:
  
  def __init__(self, vertices):
    
    self.vertices = vertices
    self.graph = defaultdict(list)
    
  def addEdge(self,v,w):
    self.graph[v].append(w)
    self.graph[w].append(v)
  
  def isCyclic(self):
    
    visited = []
    
    for i in range(self.vertices):
      if i not in visited:
        if self.isCyclicUtil(i, -1, visited):
          return True
  
    return False
    
  def isCyclicUtil(self, node, parent, visited):
    
    visited.append(node)
    
    for i in self.graph[node]:
      if i not in visited:
        
        if self.isCyclicUtil(i, node, visited):
          return True
      elif parent != i:
        return True
          
    return False
    
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(0, 3)
g.addEdge(3, 4)

print g.isCyclic()