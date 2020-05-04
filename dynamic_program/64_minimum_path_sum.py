#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
"""

import numpy as np


def min_path_sum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m, n = len(grid), len(grid[0])
    steps = np.zeros((m, n), dtype=np.int64)
    steps[0, 0] = grid[0][0]
    for i in range(1, m):
        steps[i, 0] = steps[i-1, 0] + grid[i][0]
    for j in range(1, n):
        steps[0, j] = steps[0, j-1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            steps[i, j] = min(steps[i-1, j], steps[i, j-1]) + grid[i][j]
    return int(steps[m-1][n-1])


if __name__ == '__main__':
    mat = [
        [1, 3, 1],
        [1, 2, 1],
        [4, 0, 1]
    ]

    # mat = [
    #     [1, 3, 1],
    #     [1, 5, 1],
    #     [4, 2, 1]
    # ]
    print(min_path_sum(mat))


