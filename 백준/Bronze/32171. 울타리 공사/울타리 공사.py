import sys
input = sys.stdin.readline

# (min_x, min_y) (max_x, max_y)

N = int(input().strip())
min_x, min_y = float('inf'), float('inf')
max_x, max_y = float('-inf'), float('-inf')

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    
    min_x = min(min_x, x1)
    min_y = min(min_y, y1)
    max_x = max(max_x, x2)
    max_y = max(max_y, y2)
    
    perimeter = 2 * ((max_x - min_x) + (max_y - min_y))
    print(perimeter)