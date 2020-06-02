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


def forbid(x):
    if x <= 1:
        return [2]
    if x >= n:
        return [n - 1]
    return [x - 1, x + 1]


def check(result):
    for i in range(0, len(result)-1):
        for j in range(i+1, len(result)):
            if abs(result[j] - result[i]) == j-i:
                return False
    return True


def queue(visited, rest, forbidden, results=None):
    """
    虽然添加check()函数后结果正确，但当n大于10时，计算时间过长，只用'forbidden'来剪枝效果较差。
    """
    if results is None:
        results = []

    if len(rest) <= 0:
        if check(visited):
            results.append(visited.copy())
        return

    for i, r in enumerate(rest):
        if r in forbidden:
            continue

        visited.append(r)
        rest.pop(i)
        queue(visited, rest, forbid(r), results=results)
        visited.pop(-1)
        rest.insert(i, r)

    return results


def to_board(results):
    boards = []
    for result in results:
        board = [list("."*n) for i in range(n)]
        for i, r in enumerate(result):
            board[r-1][i] = "Q"
        boards.append(list(map("".join, board)))
    return boards


n = 4
rlts = queue([], [i for i in range(1, n+1)], [])
print(len(rlts))
# print(rlts)
# print(to_board(rlts))

for n in range(1, 20):
    print(n, "queue result:", len(queue([], [i for i in range(1, n+1)], [])))


