#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
"""


# Recursion
def recursion(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    return recursion(n-1) + recursion(n-2)


#
def forward(n):
    if n <= 2:
        return n

    ppre, pre, now = 1, 2, 0
    count = 3   # 从第3步开始
    while True:
        if count > n:
            break
        now = ppre + pre
        ppre = pre
        pre = now
        count += 1
    return now


if __name__ == '__main__':
    print(recursion(10))
    print(forward(10))

