import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lit_dict = {}

for i in range(1, n+1):
    string = input().rstrip()
    lit_dict[str(i)] = string
    lit_dict[string] = i

for _ in range(m):
    temp = input().rstrip()
    print(lit_dict[temp])