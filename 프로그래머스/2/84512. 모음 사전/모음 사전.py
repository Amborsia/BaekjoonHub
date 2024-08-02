from itertools import product
def solution(word):
    vowels = ['A','E','I','O','U']
    dict = []
    
    for i in range(1,6):
        for comb in product(vowels, repeat = i):
            dict.append(''.join(comb))
    dict.sort()
    return dict.index(word)+1