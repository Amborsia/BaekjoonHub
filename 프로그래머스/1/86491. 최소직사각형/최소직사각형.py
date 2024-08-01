def solution(sizes):
    max_height, max_width = 0,0
    for w,h in sizes:
        if w<h:
            w,h = h,w
        max_width = max(max_width,w)
        max_height = max(max_height,h)
    return max_width*max_height