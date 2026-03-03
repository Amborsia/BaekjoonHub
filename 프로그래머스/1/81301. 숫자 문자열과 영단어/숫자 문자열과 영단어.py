def solution(s):
    answer = ''
    dicts = {"zero":0, "one":1,"two":2,"three":3,"four":4, "five":5,
           "six":6, "seven":7, "eight":8, "nine":9}
    start = 0
    idx= 0
    print()
    while idx <= len(s):
        idx+=1
        value = s[start:idx]
        if value in dicts:
            start = idx
            answer+=str(dicts[value])
        elif value.isdigit():
            start = idx
            answer+=str(value)
            
            
    return int(answer)