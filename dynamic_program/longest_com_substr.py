#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np


def reverse(text):
    rtext = list(text)
    m = len(rtext)
    for i in range(m // 2):
        ch = rtext[i]
        rtext[i] = rtext[m - (i + 1)]
        rtext[m - (i + 1)] = ch
    return "".join(rtext)


def max_com_sub_square(text1, text2=None):
    """
    查找两个字符串最长公共字串(可能会有多个)
    :param text1:
    :param text2: if None, set to reversed text1
    :return:
    """
    if text2 is None:
        text2 = reverse(text1)

    m, n = len(text1), len(text2)
    steps = np.zeros((m, n), dtype=np.int32)
    for i in range(m):
        for j in range(n):
            steps[i, j] = 1 if text1[i] == text2[j] else 0
    for i in range(1, m):
        for j in range(1, n):
            if steps[i - 1, j - 1] >= 1 and steps[i, j] == 1:
                steps[i, j] = steps[i - 1, j - 1] + 1

    candidates = set()
    max_size = np.max(steps)
    row, col = np.where(steps == max_size)
    for r in row:
        candidates.add(text1[r - max_size + 1:r + 1])
    candidates = list(candidates)
    return candidates


if __name__ == '__main__':
    # data = ["babad", "abcdbbfcba", "abracadabra"]
    # for s in data:
    #     print(max_com_sub(s))

    data = [("baidu.com", "cn-baidu"), ("facebook.com", "facebook-cdn.net"), ("taobaoo", "taopaoo")]
    for s1, s2, in data:
        print(s1, s2)
        print(max_com_sub_square(s1, s2))
        print("-"*20)


