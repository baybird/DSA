# Filename     : shortestPath.py
# Author        : Robert.Tang
# Created       : 3/18/2017
# Last Modified :
# Description   : Finding shortest path in O(N^2)
# Python Version: 2.7

import sys

class Graph():

  def __init__(self, N, M):
    self.num = len(N); # length of vertex

    # lists
    self.__distance = [sys.maxsize] * self.num # maxsize represents infinity
    self.__visted   = [0]* self.num
    self.__prevVertex = [None]* self.num;

    # tuples
    self.__matrix = M
    self.__name   = N

  # Algorithm
  def calPaths(self, origin):
    self.origin = origin
    self.__distance[origin] = 0;

    for x in range(self.num):
      # find min index
      min = sys.maxsize
      min_index = 0

      for v in range(self.num):
        # print(v, self.__visted[v], self.__distance[v])

        if (self.__visted[v] == 0 and self.__distance[v] <= min):
            min = self.__distance[v]
            min_index = v
      # find min index END ##############################

      # set as visted
      self.__visted[min_index] = 1

      for x in range(self.num):
        if (self.__visted[x]!=1
          and self.__matrix[min_index][x] > 0
          and self.__distance[min_index] != sys.maxsize
          and (self.__distance[min_index] + self.__matrix[min_index][x]) < self.__distance[x] ):
          self.__distance[x] = self.__distance[min_index] + self.__matrix[min_index][x]
          self.__prevVertex[x] = min_index

  def showResult(self):
    print "Origin: ", self.origin
    print("Vertex\tShortest-Dist\t Prev-Vertex");
    for x in range(self.num):
      print "%d \t\t\t %s \t\t\t\t\t\t %s" % (x, self.__distance[x], self.__prevVertex[x])


###################################
# Test case
###################################
# Vertex - name of place
N = ("A", "B", "C", "D", "E");

# Adj. Matrix
M = (
  ( 0, 2, 0, 1, 0 ),
  ( 2, 0, 1, 2, 2 ),
  ( 0, 1, 0, 0, 2 ),
  ( 1, 2, 0, 0, 3 ),
  ( 0, 2, 2, 3, 0 ),
);

Adj = Graph(N, M);
Adj.calPaths(0)   # origin 0:A
Adj.showResult()

# Output ############################################
#
# Origin:  0
# Vertex  Shortest-Dist  Prev-Vertex
# 0        0             None
# 1        2             0
# 2        3             1
# 3        1             0
# 4        4             3
