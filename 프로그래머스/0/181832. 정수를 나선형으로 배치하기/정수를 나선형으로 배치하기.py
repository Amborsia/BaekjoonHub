def solution(n):
    answer = [[0]*n for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    cx,cy,d = 0,0,0
    
    for i in range(1, n*n+1):
        answer[cx][cy] = i
        
        nx = cx+dx[d]
        ny = cy+dy[d]
        
        if not (0 <= nx < n and 0 <= ny < n) or answer[nx][ny] != 0:
            
            d = (d+1)%4
            nx = cx+dx[d]
            ny = cy+dy[d]
        cx = nx
        cy = ny
            
        
    return answer