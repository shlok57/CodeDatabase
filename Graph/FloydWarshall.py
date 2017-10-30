# Shortest Distance to all nodes

class Graph:
  
  def __init__(self, vertices):
    
    self.vertices = vertices
    self.graph = []
    
  def print_sol(self):
    
    for i in  range(self.vertices):
      print(self.graph[i])
    
  def FloydWarshall(self):
    
    dist = self.graph
    for i in range(self.vertices):
      for j in range(self.vertices):
        for k in range(self.vertices):
          dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
          
    self.print_sol()
    
INF = float("inf")
g = Graph(4)
g.graph = [[0,5,INF,10],
             [INF,0,3,INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
        ]
        
g.FloydWarshall()