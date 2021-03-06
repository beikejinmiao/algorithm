#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。

示例：
输入：board = [[1,2,3],[4,0,5]]
输出：1
解释：交换 0 和 5 ，1 步完成

输入：board = [[1,2,3],[5,4,0]]
输出：-1
解释：没有办法完成谜板

输入：board = [[4,1,2],[5,0,3]]
输出：5
解释：
最少完成谜板的最少移动次数是 5 ，
一种移动路径:
尚未移动: [[4,1,2],[5,0,3]]
移动 1 次: [[4,1,2],[0,5,3]]
移动 2 次: [[0,1,2],[4,5,3]]
移动 3 次: [[1,0,2],[4,5,3]]
移动 4 次: [[1,2,0],[4,5,3]]
移动 5 次: [[1,2,3],[4,5,0]]
输入：board = [[3,2,4],[1,5,0]]
输出：14

提示：
board 是一个如上所述的 2 x 3 的数组.
board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-puzzle
"""
import copy


class Solution(object):

    def _tostr(self, matrix):
        mstr = ""
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                mstr += str(matrix[i][j])
        return mstr

    def neighbors(self, matrix):
        m, n = len(matrix), len(matrix[0])
        oi, oj = 0, 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    oi, oj = i, j

        if oi <= 0:
            horizontal = [1]
        elif oi >= m-1:
            horizontal = [m-2]
        else:
            horizontal = [oi-1, oi+1]

        if oj <= 0:
            vertical = [1]
        elif oj >= n-1:
            vertical = [n-2]
        else:
            vertical = [oj-1, oj+1]

        nbs = []
        for x in horizontal:
            # mat = matrix.copy()
            mat = copy.deepcopy(matrix)
            mat[oi][oj] = mat[x][oj]
            mat[x][oj] = 0
            nbs.append(mat)
        for y in vertical:
            # mat = matrix.copy()
            mat = copy.deepcopy(matrix)
            mat[oi][oj] = mat[oi][y]
            mat[oi][y] = 0
            nbs.append(mat)
        return nbs

    def sliding_puzzle(self, start):
        target = [[1, 2, 3],
                  [4, 5, 0]]
        if start == target:
            return 0

        step = 0
        visited = {self._tostr(start)}
        nodes = [start]
        while len(nodes) > 0:
            for _ in range(len(nodes)):
                for nearby in self.neighbors(nodes.pop(0)):
                    if nearby == target:
                        return step + 1
                    nstr = self._tostr(nearby)
                    if nstr not in visited:
                        visited.add(nstr)
                        nodes.append(nearby)
            step += 1
        return -1


class SolutionOpt(object):
    """
    将二维数组转成一维字符串，加快邻居节点计算和比较速度，总体速度提升两倍
    参考链接: 益智游戏克星：BFS暴力搜索算法, https://mp.weixin.qq.com/s/Xn-oW7QRu8spYzL3B6zLxw
    """
    neighbor_map = [
        {1, 3},
        {0, 4, 2},
        {1, 5},
        {0, 4},
        {3, 1, 5},
        {4, 2}
    ]

    def neighbors(self, text):
        zix = text.index("0")
        nb_idx = SolutionOpt.neighbor_map[zix]
        nbs = []
        for nix in nb_idx:
            words = list(text)
            words[zix] = words[nix]
            words[nix] = "0"
            nbs.append("".join(words))
        return nbs

    def sliding_puzzle(self, start):
        target = "123450"
        m, n = len(start), len(start[0])
        start = "".join(map(str, [start[i][j] for i in range(m) for j in range(n)]))
        step = 0
        visited = {start}
        nodes = [start]
        while len(nodes) > 0:
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                if node == target:
                    return step

                for nearby in self.neighbors(node):
                    if nearby not in visited:
                        nodes.append(nearby)
                        visited.add(nearby)
            step += 1
        return -1


if __name__ == '__main__':
    board = [[1, 2, 3],
             [4, 0, 5]]
    # board = [[1, 2, 3],
    #          [5, 4, 0]]
    # board = [[4, 1, 2],
    #          [5, 0, 3]]
    # board = [[3, 2, 4],
    #          [1, 5, 0]]
    print(Solution().sliding_puzzle(board))
    print(SolutionOpt().sliding_puzzle(board))


