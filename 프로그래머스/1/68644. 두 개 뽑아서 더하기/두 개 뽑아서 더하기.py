from itertools import combinations
def solution(numbers):
    temp = list()
    for i,j in combinations(numbers,2):
        temp.append(i+j)
    answer = sorted(list(set(temp)))
    return answer