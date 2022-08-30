def solution(files):
    dictionary = {}
    for file in files:
        dictionary[file] = list()
        head, number = '', ''
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                for j in range(len(number)): #tail은 버리기
                    if not number[j].isdigit():
                        number = number[:j]
                        break
                break
        dictionary[file].extend([head.lower(), int(number)])
    dictionary = dict(sorted(dictionary.items(), key = lambda item: item[1]))
    return list(dictionary.keys())
