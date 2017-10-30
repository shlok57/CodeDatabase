class Graph():
  
  def __init__(self, vertices):
    
    self.vertices = vertices
    self.graph = []
    
  def print_sol(self, distList):
    
    for ver in range(self.vertices):
      print ver, "\t", distList[ver]
      
  def min_dist(self, distList, visited):
    
    min = 99999
    for ver in range(self.vertices):
      
      if distList[ver] < min and ver not in visited:
        min = distList[ver]
        min_ver = ver
    
    return min_ver
      
  def Dijsktra(self, start):
    
    distList = [99999] * self.vertices
    visited = []
    distList[start] = 0
    
    for node in range(self.vertices):
       min_node = self.min_dist(distList, visited)
       visited.append(min_node)
       
       for ver in range(self.vertices):
         
         if self.graph[min_node][ver] and ver not in visited and distList[ver] > distList[min_node] + self.graph[min_node][ver]:
           distList[ver] = distList[min_node] + self.graph[min_node][ver]
    
    self.print_sol(distList)           


g  = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ];
 
g.Dijsktra(0)
      