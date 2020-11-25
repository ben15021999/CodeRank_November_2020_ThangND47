#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countPaths' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#

mod = int(1e9)
visited = [False] * (10000 + 1)
f = [0] * (10000 + 1)
cur_path = []

cycle = set()
path = set()

def check_infinity():
    for u in cycle:
        if u in path:
            return True
    return False

def dfs(u, n, lst):
    visited[u] = True
    cur_path.append(u)
    if u == n:
        update_path(1)
    elif u in lst:
        for v in lst[u]:
            if visited[v]:
                update_cycle(v)
            else:
                if f[v] > 0:
                    update_path(f[v])
                if f[v] == 0:
                    dfs(v, n, lst)
    if f[u] == 0:
        f[u] = -1
    visited[u] = False
    cur_path.pop()

def update_cycle(node):   
    p = -1     
    for i in range(len(cur_path) - 1, -1, -1):
        if cur_path[i] == node:
            break
        cycle.add(cur_path[i])
    cycle.add(node)
    
def update_path(amt):
    for u in cur_path:
        path.add(u)
        f[u] = (f[u] + amt) % mod 

def countPaths(n, edges):
    # Write your code here
    lst = {}
    for edge in edges:
        if edge[0] not in lst:
            lst[edge[0]] = []
            lst[edge[0]].append(edge[1])
        else:
            lst[edge[0]].append(edge[1])
    dfs(1, n, lst)
    if check_infinity():
        print ("INFINITE PATHS")
    else:
        print(f[1])

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    nodes = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    countPaths(nodes, edges)
