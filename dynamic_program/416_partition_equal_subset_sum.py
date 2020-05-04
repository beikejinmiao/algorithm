#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
416. 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
 
示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
"""
import numpy as np


def can_partition_lucky(nums):
    """
    靠求和奇数判断,凑巧通过而已
    :param nums:
    :return:
    """
    values = capacities = nums
    n, C = len(values), sum(capacities)
    if C % 2 > 0:       # 如果只包含正整数的数组和是奇数，那么不可能被分割成两个元素和相等的子集
        return False

    C = int(C / 2)  # + C % 2
    steps = np.zeros((n+1, C+1), dtype=np.int64)
    for i in range(1, n+1):
        ix = i - 1      # the index of values&capacities array
        vi, ci = values[ix], capacities[ix]
        if ci > C:      # 可以观察对比steps发现此处条件不合理
            steps[i, :] = steps[i-1, :]
        else:
            for c in range(ci, C+1):
                steps[i, c] = max(steps[i-1, c], steps[i-1, c-ci] + vi)
    # print(steps)    # !!!结果不准确，例如[1, 2, 8, 4, 2]，最大值竟然是8，应该是9
    if steps[n, C] == C:
        return True
    return False


def can_partition_correct(nums):
    values = capacities = nums
    n, C = len(values), sum(capacities)
    # if C % 2 > 0:
    #     return False
    C = int(C / 2) + C % 2
    steps = np.zeros((n+1, C+1), dtype=np.int64)
    for i in range(1, n+1):
        ix = i - 1          # the index of values&capacities array
        vi, ci = values[ix], capacities[ix]
        for j in range(1, C+1):
            if ci > j:
                steps[i, j] = steps[i-1, j]
            else:
                steps[i, j] = max(steps[i-1, j], steps[i-1, j-ci] + vi)
    print(steps)
    if steps[n, C] == C and sum(capacities) % 2 == 0:
        return True
    return False


"""
针对[1, 2, 8, 4, 2]
can_partition_lucky()结果：
[[0 0 0 0 0 0 0 0 0 0]
 [0 1 1 1 1 1 1 1 1 1]
 [0 0 2 3 3 3 3 3 3 3]      
 [0 0 0 0 0 0 0 0 8 8]      # '8'之前竟然都是0，意味着当背包空间剩余1-7时，竟然没有放进去一件东西
 [0 0 0 0 4 4 4 4 8 8]
 [0 0 2 2 4 4 6 6 8 8]]
can_partition_correct()结果：
 [[0 0 0 0 0 0 0 0 0 0]
 [0 1 1 1 1 1 1 1 1 1]
 [0 1 2 3 3 3 3 3 3 3]
 [0 1 2 3 3 3 3 3 8 9]
 [0 1 2 3 4 5 6 7 8 9]
 [0 1 2 3 4 5 6 7 8 9]]
"""


def can_partition_opt(nums):
    """
    优化空间复杂度
    :param nums:
    :return:
    """
    values = capacities = nums      #
    n, C = len(values), sum(capacities)
    C = int(C / 2) + C % 2
    steps = np.zeros(C+1, dtype=np.int64)
    for i in range(n):
        vi, ci = values[i], capacities[i]
        if ci <= C:
            for c in reversed(range(ci, C+1)):
                steps[c] = max(steps[c], steps[c-ci] + vi)
    print(steps)
    if steps[C] == C and sum(capacities) % 2 == 0:
        return True
    return False


print(can_partition_lucky([1, 2, 8, 4, 2]))
print(can_partition_correct([1, 2, 8, 4, 2]))
print(can_partition_opt([1, 2, 8, 4, 2]))
print(can_partition_opt([1, 5, 11, 5]))
