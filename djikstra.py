from adjacencyList import *
def dijkstra(G, s):
  P = {} # permanent labels of SDs
  T = {} # temporary labels, upper bound on SDs
  P[s] = 0
  def a(s,j):
    if j not in s.getConnections():
      return inf
    else:
      return s.getWeight(j)
  for j in G.getVertices():
    T[j] = a(s,j)
  
  while P.keys() != G.getVertices():
    
    
    
  
    
