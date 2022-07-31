#백준 10825
def solution(students):
    for name, _, _, _ in sorted(students, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0])):
        print(name)
n = int(input())
students = [input().split() for _ in range(n)]
solution(students)