#자기 자신 제외 time 증가
def update_cache_times(cache, city):
    for k, _ in cache.items():
        if k == city: cache[k] = 0
        else: cache[k] += 1
            
def get_max_time(cache):
    key = 0
    biggest = -float('inf')
    for k, v in cache.items():
        if biggest < v:
            key = k
            biggest = v
    return key

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = dict()
    total = 0
    for city in cities:
        if city.lower() in cache:
            total += 1
        else:
            if len(cache) < cacheSize:
                cache[city.lower()] = 0
            elif len(cache) == cacheSize:
                out_city = get_max_time(cache)
                cache.pop(out_city)
                cache[city.lower()] = 0
            total += 5
        update_cache_times(cache, city.lower())
    return total

print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))