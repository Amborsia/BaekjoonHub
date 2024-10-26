import sys
input = sys.stdin.readline

a = int(input().rstrip())

if a >= 3000:
    print("book")
elif a >= 1000:
    print("mask")
elif a >= 500:
    print("pen")
else:
    print("no")