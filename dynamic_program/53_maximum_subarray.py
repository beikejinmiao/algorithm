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

# 参考
# https://www.cnblogs.com/AlvinZH/p/6795647.html
# https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode/


def max_sub_sum_cube(nums):
    # 时间复杂度：O(n^3)
    m = len(nums)
    steps = np.zeros((m, m), dtype=np.int32)
    for i in range(m):
        for j in range(i, m):
            steps[i, j] = sum(nums[i:j+1])
    return np.max(steps)


def max_sub_sum_square(nums):
    # 时间复杂度：O(n^2)
    m = len(nums)
    sums = [0 for i in range(m)]
    sums[0] = nums[0]
    for i in range(1, m):
        sums[i] = sums[i-1] + nums[i]
    steps = np.zeros((m, m), dtype=np.int32)
    for i in range(m):
        for j in range(i, m):
            steps[i, j] = sums[j] - sums[i]
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


# 分治法 Divide and Conquer
def max_sub_sum_dc(nums):
    # 时间复杂度：O（nlgn）
    m = len(nums)
    if m <= 1:
        return nums[0]
    # elif m == 2:
    #     return max(nums[0], nums[1], sum(nums))

    center = int(m/2)
    submax = max(max_sub_sum_dc(nums[:center]), max_sub_sum_dc(nums[center:]))  # smax(解只在左边，解只在右边)

    # 解跨越左右子数组
    lmax, lsum = nums[center-1], 0
    for i in range(1, center+1):
        lsum += nums[center-i]
        if lsum > lmax:
            lmax = lsum
    rmax, rsum = nums[center], 0
    for i in range(center, m):
        rsum += nums[i]
        if rsum > rmax:
            rmax = rsum
    return max(submax, lmax+rmax)


if __name__ == '__main__':
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sub_sum_square(array))
    print(max_sub_sum_linear2(array))
    print(max_sub_sum_dc(array))


