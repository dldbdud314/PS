from heapq import heappush, heappop

def solution(food_times, k):
    if sum(food_times) <= k: #edge case
        return -1
    heap = []
    for num, time in enumerate(food_times):
        heappush(heap, (time, num + 1))
    prev_time = 0
    while heap:
        cur_time, num = heap[0]
        time_taken = len(heap) * (cur_time - prev_time) #남은 음식 개수*걸린 시간
        if k >= time_taken:
            k -= time_taken
            heappop(heap)
            prev_time = cur_time
        else:
            break
    if heap: 
        food_nums = list(map(lambda x:x[1], heap))
        food_nums.sort()
        return food_nums[k % len(food_nums)]
    else:
        return -1