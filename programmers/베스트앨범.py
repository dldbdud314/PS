from collections import defaultdict

def solution(genres, plays):
    songs = defaultdict(list) #음악 장르, 재생 횟수
    total_list = []#합 저장
    ids = [i for i in range(len(genres))]
    for id, genre, play in zip(ids, genres, plays):
        songs[genre].append((id, play))
    for k, v in songs.items():
        v.sort(key=lambda x: x[1], reverse=True)
        total = 0
        for vv in v: total+=vv[1]
        total_list.append([k, total])
    total_list.sort(key= lambda x : x[1], reverse=True)
    ans = []
    for g, _ in total_list:
        ans.append(songs[g][0][0])
        if len(songs[g]) > 1:
            ans.append(songs[g][1][0])
    return ans
    
print(solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 150, 800, 2500]))