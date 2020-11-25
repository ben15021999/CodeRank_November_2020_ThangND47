#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    dct = {}
    arr = []
    for i in range(len(price)):
        dct[i] = price[i]
    for k, v in sorted(dct.items(), key = lambda item: item[1]):
        arr.append([k, v])
    ans = 10e17
    for i in range(1, len(price)):
        if arr[i][0] < arr[i - 1][0]:
            ans = min(ans, arr[i][1] - arr[i - 1][1])
    return ans 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
