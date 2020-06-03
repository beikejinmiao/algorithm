#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np

"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
"""


def max_palindrome(text):
    text = str(text).strip()
    m = len(text)
    if m <= 1:
        return text

    max_size = 1
    candidates = set()
    pdrome = ""
    for i in range(m):
        # 如果当前字符和下一个字符相等，则保存当前字符直接进入下一轮
        if i + 1 < m and text[i] == text[i + 1]:
            pdrome += text[i]
            continue
        pdrome += text[i]
        existed_size = len(pdrome) - 1
        for j in range(1, min(i, m-i-1) + 1):
            # 向两边扩展
            left, right = (i-existed_size)-j, i+j
            if left < 0 or right >= m or text[left] != text[right]:
                # 越界或者左右对称位置的字符不相等，停止
                break
            pdrome = "%s%s%s" % (text[left], pdrome, text[right])
        if len(pdrome) >= max_size:
            candidates.add(pdrome)
            max_size = len(pdrome)
        # 清空进行下一轮
        pdrome = ""
    # 由于想获取所有最长回文子串，那“最长”肯定是慢慢变长，所以可能会保存次长、次次长等等子串，需移除
    candidates = [c for c in candidates if len(c) >= max_size]
    return candidates[0]


def max_palindrome_grace(text):
    """
    逻辑更清晰但效率相对于另一种方案低些
    https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484471&idx=1&sn=7c26d04a1f035770920d31377a1ebd42
    :param text:
    :return:
    """
    def palindrome(l, r):
        # 判断停止条件并防止越界
        while l >= 0 and r < len(text) and text[l] == text[r]:
            # 向两边扩展
            l -= 1
            r += 1
        return text[l+1:r]      # 一定要注意python字符串截取时,最右侧是不包含

    result = ""
    for i in range(len(text)):
        # 以text[i]为中心的最长回文子串
        rlt1 = palindrome(i, i)
        # 以text[i]和text[i+1]为中心的最长回文子串
        rlt2 = palindrome(i, i + 1)
        result = rlt1 if len(rlt1) > len(result) else result
        result = rlt2 if len(rlt2) > len(result) else result
    return result


if __name__ == '__main__':
    data = ["", "a", "ab", "abb", "aab", "aba", "cbbd", "cbbbd", "cbbbbd", "babad", "abcdbbfcba", "abracadabra"]
    for s in data:
        print(s)
        print(max_palindrome(s))
        print(max_palindrome_grace(s))
        print("-"*20)

    data2 = ["abcba"]
    for s in data2:
        print(s)
        print(max_palindrome(s))
        print(max_palindrome_grace(s))
        print("-"*20)

    print(max_palindrome("d"*1000))
    print(max_palindrome_grace("d" * 1000))




