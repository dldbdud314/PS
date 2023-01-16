import math

n = int(input())
stores = list(map(int, input().split()))
k, l = map(int, input().split())

total = 0
for store in stores:
    if store <= k:
        total += 1
        continue
    store -= k
    total += (math.ceil(store / l) + 1)

print(total)