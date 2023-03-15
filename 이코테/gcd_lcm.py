import math

arr = [2, 4, 8, 10, 12]

# 최대 공약수
gcd = arr[0]
for i in range(1, len(arr)):
    gcd = math.gcd(arr[i], gcd)

# 최소 공배수
lcm = arr[0]
for i in range(1, len(arr)):
    lcm = math.lcm(arr[i], lcm)

print(gcd)
print(lcm)
