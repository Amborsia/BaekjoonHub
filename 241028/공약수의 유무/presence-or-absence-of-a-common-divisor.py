import sys
input = sys.stdin.readline
a,b = list(map(int,input().split()))
lit_a = []
lit_b = []
for i in range(1,a+1):
    if a%i == 0:
        lit_a.append(i)
for i in range(1,b+1):
    if a%i == 0:
        lit_b.append(i)

max_len = len(lit_b) if len(lit_b)>=len(lit_a) else len(lit_a)
IsFinish = False
for i in range(max_len):
    if lit_b[i] in lit_a:
        IsFinish =True
        break
if IsFinish == False:
    print(0)
else:
    print(1)