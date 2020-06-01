#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
全排列

回溯算法详解: https://mp.weixin.qq.com/s/nMUHqvwzG2LmWA9jMIHwQQ
"""


def perror(track, rest, results=None):
    if results is None:
        results = []

    if len(rest) <= 0:
        results.append(track)
        return

    for i, r in enumerate(rest):
        print("========================>>")
        print("before current: ", r)
        print("before 1, track: ", track, "rest: ", rest)
        track.append(r)
        rest = rest[:i] + rest[i+1:]
        print("before 2, track: ", track, "rest: ", rest)
        perror(track, rest, results=results)
        print("after current: ", r)
        print("after 1, track: ", track, "rest: ", rest)
        # 此处新建track对象,虽然变量名都是'track',但和20行的track已经不是一个对象;
        # 所以此处其实没有真的删除track的最后一个值,只是在不断重复新建对象而已.
        track = track[:-1]
        rest.insert(i, r)
        print("after 2, track: ", track, "rest: ", rest)
        print("<<========================")

    return results


print(perror([], [1, 2, 3]))


def permutation(track, rest, results=None):
    if results is None:
        results = []

    if len(rest) <= 0:
        results.append(track.copy())     # track在整个递归计算过程中都是同一个,所以此时必须copy保存当前状态
        return

    for i, r in enumerate(rest):
        track.append(r)
        # rest.pop(i)
        rest = rest[:i] + rest[i + 1:]      # 剩余列表可以新建,为啥?!
        permutation(track, rest, results=results)
        # track = track[:-1]    # 不能新建对象,必须改变原来的(即append的)track
        track.pop(-1)
        rest.insert(i, r)

    return results


def permutation2(track, rest, results=None):
    if results is None:
        results = []

    if len(rest) <= 0:
        results.append(track)
        return

    for i, r in enumerate(rest):
        if r in track:
            continue

        track.append(r)
        rest = rest[:i] + rest[i+1:]
        permutation(track, rest, results=results)
        track = track[:-1]
        rest.insert(i, r)

    return results


print(permutation([], [1, 2, 3]))
print(permutation2([], [1, 2, 3]))





