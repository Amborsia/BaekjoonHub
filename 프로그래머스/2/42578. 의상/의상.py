def solution(clothes):
    dict = {}
    
    for _, kind in clothes:
        if kind in dict:
            dict[kind]+=1
        else:
            dict[kind]=1
    combo = 1
    for count in dict.values():
        combo *= (count+1)
        
    return combo-1