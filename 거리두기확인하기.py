def checkDis(room):
    for y in range(len(room)):
        for x in range(len(room)):
            if room[x][y] == 'P':
                if y-1 >= 0 and room[x][y-1] == 'P': return 0
                if x+1 < len(room) and room[x+1][y] == 'P': return 0
                if y+1 < len(room) and room[x][y+1] == 'P': return 0
                if y-1 >= 0 and room[x][y-1] == 'P': return 0
                if x+1 < len(room) and y-1 >= 0 and room[x+1][y-1] == 'P':
                    if room[x][y-1] == 'O' or room[x+1][y] == 'O': return 0
                if x+1 < len(room) and y+1 < len(room) and room[x+1][y+1] == 'P': 
                    if room[x][y+1] == 'O' or room[x+1][y] == 'O': return 0
                if x-1 >= 0 and y+1 < len(room) and room[x-1][y+1] == 'P': 
                    if room[x][y+1] == 'O' or room[x-1][y] == 'O': return 0
                if x-1 >= 0 and y-1 >= 0 and room[x-1][y-1] == 'P': 
                    if room[x][y-1] == 'O' or room[x-1][y] == 'O': return 0
                if y-2 >= 0 and room[x][y-2] == 'P': 
                    if room[x][y-1] == 'O': return 0
                if x+2 < len(room) and room[x+2][y] == 'P': 
                    if room[x+1][y] == 'O': return 0
                if y+2 < len(room) and room[x][y+2] == 'P': 
                    if room[x][y+1] == 'O': return 0
                if x-2 >= 0 and room[x-2][y] == 'P': 
                    if room[x-1][y] == 'O': return 0
    return 1

def solution(places):
    answer = []
    for p in places:
        answer.append(checkDis(p))
                    
    return answer
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))