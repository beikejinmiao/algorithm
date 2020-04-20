#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np

"""
https://leetcode-cn.com/problems/longest-palindromic-substring/
"""


def max_palindrome_square(text):
    """ 超出时间限制 """
    text = str(text).strip()
    if len(text) <= 1:
        return text

    text = " %s " % " ".join(list(text))
    # print(text)
    m = len(text)
    steps = np.zeros((m-1, m-1), dtype=np.int32)
    # print(steps.shape)
    for i in range(1, m-1):
        for j in range(1, min(i, m-1-i)+1):
            left, right = text[i - j], text[i + j]
            if left != right:
                break
            steps[i, j] = steps[i, j-1] + 2
    # print(steps)

    candidates = set()
    max_size = np.max(steps)
    rows, cols = np.where(steps == max_size)
    for i in range(len(rows)):
        row, col = rows[i], cols[i]
        candidates.add(text[row-col:row+col+1].replace(" ", ""))
    candidates = list(candidates)
    return candidates[0]


if __name__ == '__main__':
    # data = ["", "a", "ab", "abb", "aab", "aba", "cbbd", "cbbbd", "cbbbbd", "babad", "abcdbbfcba", "abracadabra"]
    # for s in data:
    #     print(s)
    #     print(max_palindrome(s))
    #     print("-"*20)

    print(max_palindrome_square("d"*1000))




