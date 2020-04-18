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


def max_com_sub(text1, text2=None):
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


def lcsubstr(src, dst):
    """
    Longest Common Substring
    :param src:
    :param dst:
    :return:
    """
    m = [[0 for i in range(len(dst) + 1)] for j in range(len(src) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    mmax = 0      # 最长匹配的长度
    p = 0         # 最长匹配对应在s1中的最后一位
    for i in range(len(src)):
        for j in range(len(dst)):
            if src[i] == dst[j]:
                m[i+1][j+1] = m[i][j]+1
                if m[i+1][j+1] > mmax:
                    mmax = m[i+1][j+1]
                    p = i+1
    return src[p-mmax:p], mmax   # 返回最长子串及其长度


if __name__ == '__main__':
    # data = ["babad", "abcdbbfcba", "abracadabra"]
    # for s in data:
    #     print(max_com_sub(s))

    data = [("baidu.com", "cn-baidu"), ("facebook.com", "facebook-cdn.net"), ("taobaoo", "taopaoo")]
    for s1, s2, in data:
        print(s1, s2)
        print(max_com_sub(s1, s2))
        print(lcsubstr(s1, s2))
        print("-"*20)


