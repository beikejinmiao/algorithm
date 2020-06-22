#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
items = [4, 324, 213, 223, 14, 356, 5, 6, 901, 901, 4657, 23, 5768, 56, 786, 921, 123]
# [5768, 4657, 921, 901, 901, 786, 356, 324, 223, 213, 123, 56, 23, 14, 6, 5, 4]


def bsearch(nums, v):
    size = len(nums)
    if size <= 0:
        return 0
    if size == 1:
        if v < nums[0]:
            return 1
        return 0

    ix = size // 2
    c = nums[ix]
    if v == c:
        return ix
    if v < c:
        return ix + bsearch(nums[ix+1:], v) + 1
    return bsearch(nums[:ix], v)


def topk(nums, k=3):
    k = min(k, len(nums))
    arr = [-sys.maxsize]
    for v in nums:
        # for i in range(k):      # O(n*k)
        #     if v >= arr[i]:
        #         arr.insert(i, v)
        #         break
        arr.insert(bsearch(arr, v), v)   # 二分查找: O(n*log(k))
    return arr[:k]


def kth(nums, k=3):
    # https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
    if len(nums) <= 0:
        raise Exception("num array is empty")
    return topk(nums, k=k)[-1]


def bubble_opt(nums):
    # 冒泡排序优化版，时间复杂度O(n*log(n))
    return topk(nums, k=len(nums))


print(bubble_opt([]))
print(bubble_opt(items))
print(topk(items, k=len(items)//2))
print(kth(items, k=5))
print(kth([1], k=5))


# for x in [9999, 4656, 888, 7, 1]:
#     _nums = [5768, 4657, 921, 901, 901, 786, 356, 324, 223, 213, 123, 56, 23, 14, 6, 5, 4]
#     _nums.insert(bsearch(_nums, x), x)
#     print(x, "->", _nums)

