#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 1 or n <= 1:
            return 1

        steps = np.zeros((m, n), dtype=np.int32)
        steps[0, :] = 1
        steps[:, 0] = 1
        for i in range(1, m):
            for j in range(1, n):
                steps[i, j] = steps[i-1, j] + steps[i, j-1]
        return int(steps[m-1, n-1])


# print(Solution().uniquePaths(3, 3))


class Solution2(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        grid = np.array(obstacleGrid)
        print(grid)
        m, n = grid.shape  # len(grid), len(grid[0])
        if grid[0, 0] == 1 or grid[m-1, n-1] == 1:
            return 0
        steps = np.zeros(grid.shape, dtype=np.int32)

        hits = np.where(grid[0, :] == 1)[0]
        obstacle = n + 1
        if len(hits) > 0:
            obstacle = hits[0]
        steps[0, 0:obstacle] = 1

        hits = np.where(grid[:, 0] == 1)[0]
        obstacle = m + 1
        if len(hits) > 0:
            obstacle = hits[0]
        steps[0:obstacle, 0] = 1

        print(steps)

        for i in range(1, m):
            for j in range(1, n):
                left = up = 0
                if grid[i-1, j] == 0:
                    left = steps[i - 1, j]
                if grid[i, j-1] == 0:
                    up = steps[i, j-1]

                steps[i, j] = left + up

        return int(steps[m-1, n-1])


# mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# print(Solution2().uniquePathsWithObstacles(mat))


print(np.array([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))

