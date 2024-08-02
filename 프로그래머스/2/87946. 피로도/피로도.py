from itertools import permutations
def solution(k, dungeons):
    max_explored = 0

    for order in permutations(dungeons):
        current_fatigue = k
        explored_count = 0

        for minimum, consumption in order:
            if current_fatigue >= minimum:
                current_fatigue -= consumption
                explored_count+=1
            else:
                break
        max_explored = max(max_explored,explored_count)
    return max_explored