import sys

class Solution():

    def numOfIslands(self, grid):
        count = 0;
        self.__n = len(grid);
        # print "n:", self.__n
        if self.__n == 0:
            return 0;

        self.__m = len(grid[0]);
        # print "m:",self.__m

        for i in xrange(self.__n):
            for j in xrange(self.__m):
                if (grid[i][j] == 1):
                    # print "search:", i, j
                    self.DFS(grid, i, j);
                    # print "count:", count
                    count +=1;

        return count;

    def DFS(self, grid, i, j):
        if (i < 0 or j < 0
            or i >= self.__n or j >= self.__m
            or grid[i][j] != 1):
            return;

        grid[i][j] = '0'; # marking
        self.DFS(grid, i + 1, j); # down
        self.DFS(grid, i - 1, j); # up
        self.DFS(grid, i, j + 1); # right
        self.DFS(grid, i, j - 1); # left

# Test
matrix = [
    [1,1,1,1,0],
    [1,1,0,0,0],
    [1,1,0,1,1],
    [0,0,1,0,0]
]

S = Solution()
num = S.numOfIslands(matrix)
print num
