def solution(s):
    lit = []
    for i in s:
        if lit and lit[-1] == i:
            lit.pop()
        else:
            lit.append(i)

    return 1 if not lit else 0