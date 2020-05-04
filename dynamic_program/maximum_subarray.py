#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
"""
import numpy as np


def max_sub_sum_square(nums):
    m = len(nums)
    steps = np.zeros((m, m), dtype=np.int32)
    for i in range(m):
        for j in range(i, m):
            steps[i, j] = sum(nums[i:j+1])
    print(steps)
    return np.max(steps)


def max_sub_sum_linear(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + max(nums[i - 1], 0)
    print(nums)
    return max(nums)


def max_sub_sum_linear2(nums):
    _max_ = max(nums)
    _sum_ = 0
    for i in range(1, len(nums)):
        _sum_ = max(nums[i], _sum_+nums[i])
        _max_ = max(_sum_, _max_)
    return _max_


if __name__ == '__main__':
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # print(max_sub_sum_square(array))
    print(max_sub_sum_linear2(array))


