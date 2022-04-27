#부분합

def get_partial_sum(s, arr):
    #edge case
    if sum(arr) < s: return 0    
    l, r, total = 0, 0, arr[0]
    min_len = float('inf')
    while r < len(arr) and l <= r:
        if total >= s:
            min_len = min(min_len, (r + 1) - l)
        if total < s and r + 1 < len(arr):
            r += 1
            total += arr[r]
        else:
            total -= arr[l]
            l += 1
    return min_len

n, s = map(int, input().split())
arr = list(map(int, input().split()))
print(get_partial_sum(s, arr))