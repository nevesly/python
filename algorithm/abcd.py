#!/bin/env python
# -*- coding: utf-8 -*-
############################################################
## @author Seven.Lu
## @copytright 2013 (c) Seven
##
## 给出一个N，给出一个N位整数 abcd...mn, 使其
##      abcd....mn * 9 = nm...dcba
############################################################

import sys, os
import itertools
import time

def gen2list(generator):
    # 把生成器转为列表
    l = list(generator)
    # 这里hardcode了一下, 头尾分别为1，9
    l.insert(0, 1)
    l.append(9)
    return l

def build_base_arr(N, base = 10):
    # 根据位数创建每一位的基数, 如 N = 4, 则: [1000, 100, 10, 1]
    l = [base ** i for i in xrange(N, -1, -1)]
    return l

def calc(N):
    N1 = N - 2
    if N1 <= 0: return []

    base_arr = build_base_arr(N)
    # 建造所有数据的列表生成器
    gen = itertools.product(xrange(0, 10), repeat=N1)
    ret = []
    for g in gen:
        l = gen2list(g)
        sum1 = list2int(l, base_arr)
        l.reverse()
        sum2 = list2int(l, base_arr)
        if sum1 * 9 == sum2:
            l.reverse()
            ret.append(l)
    return ret

def list2int(l, base_arr):
    # 把列表[1,2,3,4] 转化成1234
    length = len(l)
    acc = 0
    for i in xrange(length):
        acc += l[i] * base_arr[i]
    return acc

##########################################
# NOTE: use str 2 int, much slower
def get_max(N):
    return 10 ** N

def calc1(N):
    ret = []
    max = get_max(N)
    for i in xrange(1000, max):
        i1 = i
        si = str(i)
        si2 = si[::-1]
        i2 = int(si)
        if i1 * 9 == i2:
            ret.append(i)
    return ret

##########################################
def main(N):
    t1 = time.time()
    result = calc(N)
    t2 = time.time()

    print u"长度:", N
    print u"用时:", t2-t1
    print u"结果:", result

#
if __name__ == '__main__':
    s = int(raw_input(u"多少位: ".encode(sys.stdin.encoding)).decode(sys.stdin.encoding))
    for i in xrange(1, s + 1):
        main(i)
        print '-' * 15

