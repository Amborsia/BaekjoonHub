# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

N = int(input())
lit = list(map(int, input().split()))

start = lit.index(max(lit))
left = lit[start]
right = lit[start]

# 왼쪽으로 검사
for i in range(start - 1, -1, -1):
    if lit[i] > left:
        print(0)
        sys.exit()
    left = lit[i]

# 오른쪽으로 검사
for i in range(start + 1, N):
    if lit[i] > right:
        print(0)
        sys.exit()
    right = lit[i]

print(sum(lit))
