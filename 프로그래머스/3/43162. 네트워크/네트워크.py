def dfs(node, visited, computers):
    stack = [node]
    while stack:
        current = stack.pop()
        for near, connect in enumerate(computers[current]):
            if connect and not visited[near]:
                visited[near] = True
                stack.append(near)

def solution(n, computers):
    visited = [False]* n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i,visited, computers)
            count+=1
    return count