s = input()
lst = list(s)
lst.sort()
res = ''
total = 0
for s in lst:
    if s.isalpha():
        res += s
    else:
        total += int(s)
print(res + str(total)) if total != 0 else print(res)