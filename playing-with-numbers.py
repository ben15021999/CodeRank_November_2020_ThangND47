#!/bin/python3

import math
import os
import random
import re
import sys

def solve1(arr, sum_query, sum_arr):
    lmost = -1
    rmost = -1
    n = len(arr) - 1
    median = -1
    l = 1
    r = n
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] >= 0:
            r = m
        else:
            l = m + 1
    if arr[l] >= 0:
        median = l
    elif arr[r] >= 0:
        median = r
    else:
        median = n + 1
    l = 1
    r = n
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] >= 0:
            r = m - 1
        elif arr[m] + sum_query > 0:
            r = m
        else:
            l = m + 1
    if arr[l] < 0 and arr[l] + sum_query > 0:
        lmost = l
    elif arr[r] < 0 and arr[r] + sum_query > 0:
        lmost = r
    if lmost != -1:
        rmost = median - 1
    print(lmost, rmost)
    suml = 0
    sumr = 0
    sumbt = 0
    if rmost != -1 and lmost != -1:
        sumbt = sum_query * (rmost - lmost + 1) - 2 * (sum_arr[rmost] - sum_arr[lmost - 1])
    if lmost != -1:
        suml = sum_query * (lmost - 1)
    if rmost != -1:
        sumr = sum_query * (n - rmost)
    if rmost != -1 or lmost != -1:
        return sum_arr[n] - suml + sumr + sumbt
    return sum_arr[n] - (median - 1) * sum_query + (n - median + 1) * sum_query

def solve2(arr, sum_query, sum_arr):
    lmost = -1
    rmost = -1
    n = len(arr) - 1
    median = -1
    l = 1
    r = n
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] >= 0:
            r = m
        else:
            l = m + 1
    if arr[l] >= 0:
        median = l
    elif arr[r] >= 0:
        median = r
    else:
        median = n + 1
    l = 1
    r = n
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] <= 0:
            l = m + 1
        elif arr[m] + sum_query < 0:
            l = m
        else:
            r = m - 1
    if arr[r] > 0 and arr[r] + sum_query < 0:
        rmost = r
    elif arr[l] > 0 and arr[l] + sum_query < 0:
        rmost = l
    if rmost != -1:
        lmost = median
    suml = 0
    sumr = 0
    sumbt = 0
    sum_query = abs(sum_query)
    if rmost != -1 and lmost != -1:
        sumbt = sum_query * (rmost - lmost + 1) - 2 * (sum_arr[rmost] - sum_arr[lmost - 1])
    if lmost != -1:
        suml = sum_query * (lmost - 1)
    if rmost != -1:
        sumr = sum_query * (n - rmost)
    if rmost != -1 or lmost != -1:
        return sum_arr[n] + suml - sumr + sumbt
    return sum_arr[n] + (median - 1) * (sum_query) - (n - median + 1) * (sum_query)
    
# Complete the playingWithNumbers function below.
def playingWithNumbers(arr, queries):
    sorted_arr = sorted(arr)
    sum_arr = []
    sum_arr.append(0)
    ans = []
    sum_query = 0
    for i in range(len(arr)):
        sum_arr.append(sum_arr[i] + abs(sorted_arr[i]))
    sorted_arr.insert(0, 0)
    print(sorted_arr)
    for query in queries:
        sum_query += query
        if sum_query >= 0:
            ans.append(solve1(sorted_arr, sum_query, sum_arr))
        else:
            ans.append(solve2(sorted_arr, sum_query, sum_arr))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    q = int(input())

    queries = list(map(int, input().rstrip().split()))

    result = playingWithNumbers(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
