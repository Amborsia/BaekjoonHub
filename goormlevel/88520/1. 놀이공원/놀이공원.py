def min_waste_in_area(N, K, grid):
    # 누적 합 배열 초기화
    prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

    # 누적 합 배열 채우기
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix_sum[i][j] = grid[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
    
    min_waste = float('inf')
    
    # 각 좌표에서 KxK 영역의 폐기물 수 계산
    for i in range(K, N + 1):
        for j in range(K, N + 1):
            total_waste = prefix_sum[i][j] - prefix_sum[i-K][j] - prefix_sum[i][j-K] + prefix_sum[i-K][j-K]
            min_waste = min(min_waste, total_waste)
    
    return min_waste

# 입력 받기
number = int(input())
for i in range(number):
	
	N,K = map(int,input().split())
	grid = [list(map(int, input().split())) for _ in range(N)]

	print(min_waste_in_area(N, K, grid))
