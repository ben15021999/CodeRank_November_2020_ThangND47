#!/bin/python3

import math
import os
import random
import re
import sys

res = []

def check(a, b):
    if len(b) == 0:
        return True
    if len(a) < len(b):
        return True
    elif len(a) > len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] > b[i]:
                return False
    return True

# Complete the kFactorization function below.
def kFactorization(n, A, k, temp):
    global res
    if n == 1:
        if len(res) == 0:
            res = list(temp)
        else:
            if check(temp, res):
                res = list(temp)
        return
    if k == -1:
        return
    if n % A[k] != 0:
        kFactorization(n, A, k - 1, temp)
    else:
        cnt = 0
        while n % A[k] == 0:
            n //= A[k]
            temp.append(n)
            if not check(temp, res):
                return
            cnt += 1
        kFactorization(n, A, k - 1, temp)
        while cnt > 0:
            cnt -= 1
            temp.pop()
            n *= A[k]
            kFactorization(n, A, k - 1, temp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))
    A = sorted(A)
    res = []
    kFactorization(n, A, len(A) - 1, [])
    result = res
    if len(result) == 0:
        result.insert(0, -1)
    else:
        result.insert(0, n)
    result.reverse()
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
