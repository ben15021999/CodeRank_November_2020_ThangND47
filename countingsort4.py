#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    for i in range(int((len(arr)) / 2)):
        arr[i][1] = "-"
    dct = {}
    for i in range(len(arr)):
        arr[i][0] = int(arr[i][0])
        if arr[i][0] in dct:
            dct[arr[i][0]] = dct[arr[i][0]] + " " + arr[i][1]
        else:
            dct[arr[i][0]] = ""
            dct[arr[i][0]] = arr[i][1]
    ans = ""
    for key in sorted(dct.keys()):
        value = dct[key]
        ans = ans + value + " "
    print(ans)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
