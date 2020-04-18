#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
"""


values = [-10, 9, 20, None, None, 15, 7]


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


tree = TreeNode(values[0])
for v in values[1:]:
    if isinstance(v, (int, float)):
        node = TreeNode(v)
        tree.left = node




