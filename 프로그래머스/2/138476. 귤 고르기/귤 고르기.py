from collections import Counter
def solution(k, tangerine):
    temp = Counter(tangerine)
    sort = sorted(temp.items(), key=lambda x:x[1],reverse= True)
    count = 0
    kind_count = 0
    for size, counts in sort:
        if count >= k:
            return kind_count
        count+= counts
        kind_count+=1
    return kind_count