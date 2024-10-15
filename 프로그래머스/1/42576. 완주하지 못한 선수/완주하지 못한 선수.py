from collections import Counter

def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    for person, count in participant_count.items():
        if completion_count[person] != count:
            return person
