def solution(sizes):
    answer = 0
    maxv=0
    minv = 0
    for i in range(0,len(sizes)):
        r,l = sizes[i]
        if r>=l:
            maxv = max(r,maxv)    
            minv = max(l,minv)
        else:
            maxv = max(l,maxv)
            minv = max(r,minv)
        
            
    return minv*maxv