#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
对候选参数列表进行穷举搜索，得到所有可能的参数组合
用处见： https://blog.csdn.net/qq_39521554/article/details/86227582
"""
from collections import OrderedDict

candidates = OrderedDict()
candidates["name"] = ["alice", "bob", "cindy", "dave"]
candidates["age"] = [11, 22, 33, 44]
candidates["height"] = [111, 222, 333, 444]
candidates["weight"] = [1111, 2222, 3333, 4444]


def grid():
    values = list(candidates.values())
    if len(values) <= 0:
        return []

    results = [[v] for v in values[0]]
    for level in range(1, len(values)):
        cache = []
        for v in values[level]:
            cache.extend([r + [v] for r in results])
        results = cache
    # print("result size: ", len(results))
    return results


def to_dict(lists):
    names = candidates.keys()
    return [dict(zip(names, lst)) for lst in lists]


print(grid())
print(to_dict(grid()))

