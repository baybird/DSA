#  File Name     : shortestPath.py
#  Author        : Robert.Tang
#  Created       : 3/18/2017
#  Last Modified :
#  Description   : Finding shortest path in O(N^2)

import sys

class ShortestPath():

  def __init__(self, num, N, M):
    self.num = num;

    # lists
    self.distance = [sys.maxsize] * self.num # maxsize represents infinity
    self.visted   = [0]* self.num
    self.prevVertex = [None]* self.num;

    # tuples
    self.matrix = M
    self.name   = N

  def calPaths(self, origin):
    self.origin = origin
    self.distance[origin] = 0;

    for x in range(self.num):
      # find min index
      min = sys.maxsize
      min_index = 0

      for v in range(self.num):
        # print(v, self.visted[v], self.distance[v])

        if (self.visted[v] == 0 and self.distance[v] <= min):
            min = self.distance[v]
            min_index = v
      # find min index END ##############################

      # set as visted
      self.visted[min_index] = 1

      for x in range(self.num):
        if (self.visted[x]!=1
          and self.matrix[min_index][x] > 0
          and self.distance[min_index] != sys.maxsize
          and (self.distance[min_index] + self.matrix[min_index][x]) < self.distance[x] ):
          self.distance[x] = self.distance[min_index] + self.matrix[min_index][x]
          self.prevVertex[x] = min_index

  def showResult(self):
    print("Origin: ", self.origin)
    print("Vertex\tShortest-Dist\t Prev-Vertex");
    for x in range(self.num):
      print(x, "\t\t\t", self.distance[x],  "\t\t\t\t\t\t", self.prevVertex[x]);


###################################
# Test case
###################################
# number of vertex
num = 5

# Vertex - name of place
N = ("A", "B", "C", "D", "E");

# Matrix
M = (
  ( 0, 3, 0, 1, 0 ),
  ( 3, 0, 2, 5, 2 ),
  ( 0, 2, 0, 0, 5 ),
  ( 1, 2, 0, 0, 1 ),
  ( 0, 2, 5, 1, 0 ),
);

Adj = ShortestPath(num, N, M);
Adj.calPaths(0)   # origin 0:A
Adj.showResult()

# Origin:  0
# Vertex  Shortest-Dist  Prev-Vertex
# 0        0             None
# 1        3             0
# 2        5             1
# 3        1             0
# 4        2             3