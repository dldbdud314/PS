def solution(phone_book):
    phone_map = set()
    phone_book.sort()
    for x in phone_book:
        for i in range(1, len(x)):
            if x[0:i] in phone_map: return False
        phone_map.add(x)
    return True

print(solution(["12","123","1235","567","88"]))
