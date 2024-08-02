def solution(elements):
    n = len(elements)
    extend_elements = elements*2
    unique = set()

    for i in range(1, n+1):
        for j in range(n):
            sub_sum = sum(extend_elements[j:j+i])
            unique.add(sub_sum)
    return len(unique)
