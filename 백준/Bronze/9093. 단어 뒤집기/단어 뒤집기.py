import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(N):
    sub = list(map(str,input().rstrip().split(" ")))
    
    reversed_words = [sub[::-1] for sub in sub]
    print(" ".join(reversed_words))
    
    
