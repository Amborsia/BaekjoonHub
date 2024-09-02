from collections import defaultdict, deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)
    nodes = []
    edge_count = 0

    while queue:
        node = queue.popleft()
        nodes.append(node)
        for neighbor in graph[node]:
            edge_count += 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return nodes, edge_count // 2  # edge_count를 2로 나누는 이유는 무방향 그래프에서 간선을 중복으로 세기 때문

def find_most_dense_component(N, connections):
    graph = defaultdict(list)

    # 그래프 구성
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    max_density = 0
    best_component = []

    # 모든 노드를 탐색하면서 연결 요소 찾기
    for node in range(1, N + 1):
        if node not in visited:
            component, edges = bfs(graph, node, visited)
            num_nodes = len(component)
            if num_nodes > 0:
                density = edges / num_nodes
                if density > max_density:
                    max_density = density
                    best_component = component
                elif density == max_density:
                    # 밀도가 같으면 더 작은 숫자로 시작하는 컴포넌트를 선택
                    best_component = min(best_component, component)

    return sorted(best_component)

# 입력 받기
N, M = map(int, input().split())
connections = [tuple(map(int, input().split())) for _ in range(M)]

# 결과 출력
best_component = find_most_dense_component(N, connections)
print(" ".join(map(str, best_component)))
