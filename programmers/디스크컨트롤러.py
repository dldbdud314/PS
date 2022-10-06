# 풀참 - 스스로 아이디어 생각하기 까다롭,,
# start -> 따로 처리 표시 신경 쓰지 않아도 됨
from heapq import heappop, heappush
def solution(jobs):
    start, t, now = -1, 0, 0
    job_times = []
    jobq = []
    while t < len(jobs):
        for req_time, work_time in jobs:
            if start < req_time <= now: #현재 처리 가능한 작업 추가
                heappush(jobq, [work_time, req_time]) # 작업 처리 시간 짧은 거 우선
        if jobq:
            work_time, req_time = heappop(jobq)
            start = now #이전 작업 끝난 시점
            now += work_time #현재 작업 끝난 시점
            job_times.append(now - req_time)
            t += 1
        else:
            now += 1
    
    return sum(job_times) // len(jobs)