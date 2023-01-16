"""구현 (난이도 쉬움)"""
import sys
input = sys.stdin.readline


def isSecret(m, n, user, secret):
    if n < m:
        return False
    for i in range(0, n - m + 1):
        if user[i:i + m] == secret:
            return True
    return False


# get input
m, n, k = map(int, input().split())
secret = list(map(int, input().split()))
user = list(map(int, input().split()))

print("secret") if isSecret(m, n, user, secret) else print("normal")
