from collections import deque

def bfs(N, K):
    max_limit = 100000
    visited = [-1] * (max_limit + 1)  # 방문 배열 초기화
    queue = deque([(N, 0)])  # 시작점과 시간을 함께 저장
    visited[N] = 0

    while queue:
        current, time = queue.popleft()
        
        if current == K:
            return time
        
        # 이동 가능한 경우들
        for next_pos in (current - 1, current + 1, 2 * current):
            if 0 <= next_pos <= max_limit and visited[next_pos] == -1:
                if next_pos == 2 * current:  # 순간이동의 경우
                    queue.appendleft((next_pos, time))  # 0초 후에 이동
                else:
                    queue.append((next_pos, time + 1))
                visited[next_pos] = time + 1

N, K = map(int, input().split())
result = bfs(N, K)
print(result)
