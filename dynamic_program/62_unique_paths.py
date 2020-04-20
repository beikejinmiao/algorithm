#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np


def unique_paths(m, n):
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


def unique_paths_with_obstacles(obstacle_grid):
    """
    :type obstacle_grid: List[List[int]]
    :rtype: int
    """
    grid = np.array(obstacle_grid)
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

    for i in range(1, m):
        for j in range(1, n):
            left = up = 0
            if grid[i-1, j] == 0:
                left = steps[i - 1, j]
            if grid[i, j-1] == 0:
                up = steps[i, j-1]

            steps[i, j] = left + up

    return int(steps[m-1, n-1])


if __name__ == '__main__':
    print(unique_paths(3, 3))
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(unique_paths_with_obstacles(mat))

