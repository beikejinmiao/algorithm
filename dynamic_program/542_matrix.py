#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np

"""
https://leetcode-cn.com/problems/01-matrix/
"""


def around(matrix, i, j, m, n):
    up = below = left = right = None
    if i-1 >= 0:
        up = matrix[i-1][j]
    if i + 1 < m:
        below = matrix[i+1][j]
    if j-1 >= 0:
        left = matrix[i][j-1]
    if j+1 < n:
        right = matrix[i][j+1]
    return up, below, left, right


def any_equal(l, v):
    return any(map(lambda x: True if x == v else False, l))


def steps(matrix):
    m, n = len(matrix), len(matrix[0])
    existed = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0:
                if not any_equal(around(matrix, i, j, m, n), 0):
                    matrix[i][j] = -1
                    existed.append((i, j))
    loop = 1
    while True:
        if len(existed) <= 0:
            break
        for i, j in existed:
            if matrix[i][j] == -1 and any_equal(around(matrix, i, j, m, n), loop):
                matrix[i][j] = loop + 1
        existed = [(i, j) for i, j in existed if matrix[i][j] == -1]
        loop += 1
    return matrix


if __name__ == '__main__':
    l = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
    mat = np.array(l).reshape(6, 5)
    print(np.array(steps(mat.tolist())))
