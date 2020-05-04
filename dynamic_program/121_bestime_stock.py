#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""
import numpy as np


def max_profit_square(nums):
    """ 暴力穷举计算每一次买入卖出,然后取最大值,时间复杂度O(n^2) """
    m = len(nums)
    if m <= 0:
        return 0
    steps = np.zeros((m, m), dtype=np.int32)
    for i in range(m):
        for j in range(i, m):
            steps[i, j] = nums[j] - nums[i]
    return int(max(0, np.max(steps)))


def max_profit_linear(nums):
    if len(nums) <= 0:
        return 0

    _max_ = 0
    _min_buy = nums[0]
    for i in range(len(nums)):
        _min_buy = min(nums[i], _min_buy)
        _max_ = max(nums[i]-_min_buy, _max_)

    return _max_


def two_max_profit_linear(nums):
    if len(nums) <= 0:
        return 0

    # one buy-sell
    _max_ = max_profit_linear(nums)
    # two buy-sell
    for i in range(1, len(nums)-1):
        if nums[i] - nums[i-1] > 0:
            _max_ = max(max_profit_linear(nums[0:i+1]) + max_profit_linear(nums[i:]), _max_)
    return _max_


if __name__ == '__main__':
    array = [7, 1, 5, 3, 6, 4]
    print(two_max_profit_linear(array))

