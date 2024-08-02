def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}')
    sets = s.split('},{')
    sets = [set(map(int,x.split(','))) for x in sets]
    sets.sort()

    for i in range(len(sets)):
        for num in sets[i]:
            if num not in answer:
                answer.append(num)
    return answer