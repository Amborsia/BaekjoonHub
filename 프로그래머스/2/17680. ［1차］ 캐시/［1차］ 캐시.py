from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    
    cache = deque(maxlen=cacheSize)
    time = 0
    
    for city in cities:
        city = city.lower()
        if city in cache:
            time+=1
            cache.remove(city)
        else:
            time+=5
        cache.append(city)
    return time