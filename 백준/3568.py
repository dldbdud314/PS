#iSharp

declaration = input()
declaration = list(declaration.split())

for i in range(1, len(declaration)):
    same = declaration[0]
    variable, others = '', ''
    for c in declaration[i]:
        if c.isalpha(): variable += c
        else: 
            if c != ',' and c != ';': others += c
    for c in others[::-1]:
        if c == ']': continue
        if c == '[': same += '[]'
        else: same += c
    print(same+' '+variable+';')