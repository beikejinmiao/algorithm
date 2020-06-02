#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:
输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

提示：
皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。
当然，她横、竖、斜都可走一到七步，可进可退。（引用自 百度百科 - 皇后 ）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
"""


class SolutionTimeout(object):
    def __init__(self, n):
        self.n = n

    def forbid(self, x):
        if x <= 1:
            return [2]
        if x >= self.n:
            return [self.n - 1]
        return [x - 1, x + 1]

    def check(self, result):
        # 对角线检查
        for i in range(0, self.n-1):
            for j in range(i+1, self.n):
                if abs(result[j] - result[i]) == j-i:
                    return False
        return True

    def queue(self, visited, rest, forbidden, results=None):
        """
        虽然添加check()函数后结果正确，但当n大于10时，计算时间过长，只用'forbidden'(临近距离为1的对角线位置)来剪枝效果较差。
        """
        if results is None:
            results = []

        if len(rest) <= 0:
            if self.check(visited):
                # TODO 可以尝试提前检查对角线位置
                results.append(visited.copy())
            return

        for i, r in enumerate(rest):
            if r in forbidden:
                continue

            visited.append(r)
            rest.pop(i)
            self.queue(visited, rest, self.forbid(r), results=results)
            visited.pop(-1)
            rest.insert(i, r)

        return results

    def to_board(self, results):
        boards = []
        for result in results:
            board = [list("."*self.n) for i in range(self.n)]
            for i, r in enumerate(result):
                board[r-1][i] = "Q"
            boards.append(list(map("".join, board)))
        return boards


# N = 4
# solution = SolutionTimeout(N)
# rlts = solution.queue([], [i for i in range(1, N+1)], [])
# print(len(rlts))
# # print(rlts)
# # print(to_board(rlts))
#
# for N in range(1, 12):
#     print(N, "queue result:", len(SolutionTimeout(N).queue([], [i for i in range(1, N+1)], [])))


#
# https://mp.weixin.qq.com/s/nMUHqvwzG2LmWA9jMIHwQQ
class Solution(object):
    def __init__(self, n):
        self.n = n

    def forbid(self, x):
        # 只根据目前皇后所在行位置计算下一个皇后禁止的行位置列表,没有计算后续所有皇后禁止的行位置
        # 即只包含右上/右下,临近距离为1的对角线位置不包含所有对角线行位置
        # 所以可能存在不合法情况
        if x <= 1:
            return [2]
        if x >= self.n:
            return [self.n - 1]
        return [x - 1, x + 1]

    @staticmethod
    def check(visited, new):
        """
        对角线检查,检查最新添加的"皇后"是否和以前任意一个"皇后"在对角线上
        :param visited: 已添加的"皇后"所在行位置列表
        :param new: 新添加的"皇后"所在行位置
        :return:
        """
        n_visit = len(visited)
        for i in range(len(visited)):
            if abs(visited[i] - new) == n_visit - i:
                return False
        return True

    def queue(self, visited, rest, forbidden, results=None):
        if results is None:
            results = []

        if len(rest) <= 0:
            results.append(visited.copy())
            return

        for i, r in enumerate(rest):
            if r in forbidden:
                continue
            # 每新添一个新"皇后"时就检查对角线位置
            if not self.check(visited, r):
                continue

            visited.append(r)
            rest.pop(i)
            self.queue(visited, rest, self.forbid(r), results=results)
            visited.pop(-1)
            rest.insert(i, r)

        return results

    def to_board(self, results):
        boards = []
        for result in results:
            board = [list("."*self.n) for i in range(self.n)]
            for i, r in enumerate(result):
                board[r-1][i] = "Q"
            boards.append(list(map("".join, board)))
        return boards


for N in range(1, 15):
    print(N, "queue result:", len(Solution(N).queue([], [i for i in range(1, N+1)], [])))
