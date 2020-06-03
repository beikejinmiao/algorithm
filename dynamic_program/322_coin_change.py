#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
"""
import sys


def change(coins, amount):
    # 特殊情况1: amount=0
    if amount <= 0:
        return 0
    steps = [-1 for i in range(amount+1)]
    coins = [c for c in coins if 0 < c <= amount]
    # 特殊情况2: 所有coin都比amount大
    if len(coins) <= 0:
        return -1
    # 初始化: 当amount=coin时,数量只需1个
    for c in coins:
        steps[c] = 1
    #
    for i in range(1, amount+1):
        if steps[i] != -1:
            continue

        reachable, min_num = False, sys.maxsize
        for c in coins:
            if i - c >= 0 and steps[i-c] != -1:
                min_num = min(min_num, steps[i-c])
                reachable = True
        if reachable:
            steps[i] = 1 + min_num

    return steps[-1]


print(change([1, 2, 5], 11))
print(change([2], 3))
print(change([2], 4))


#
def recursive(coins, amount):
    return 1 + min([recursive(coins, amount-c) for c in coins])


