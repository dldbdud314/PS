# 합계 : 62.5 / 100.0 - to fix ..
def solution(n, t, m, timetable):
    before_last = "00:01"
    last_bus = "09:00"
    if n > 1:
        for _ in range(n - 1):
            before_last = last_bus
            hour, min = map(int, last_bus.split(':'))
            if min + t >= 60:
                min = min + t - 60
                hour = hour + 1
            else:
                min += t
            str_hour = '0' + str(hour) if hour < 10 else str(hour)
            str_min = '0' + str(min) if min < 10 else str(min)
            last_bus = str_hour + ':' + str_min
    start_hour, start_min = map(int, before_last.split(':'))
    end_hour, end_min = map(int, last_bus.split(':'))
    start_time = start_hour * 60 + start_min if start_hour > 0 else start_min
    end_time = end_hour * 60 + end_min if end_hour > 0 else end_min
    crew = []
    for time in timetable:
        hour, min = map(int, time.split(':'))
        crew_time = hour * 60 + min if hour > 0 else min
        if start_time <= crew_time <= end_time:
            crew.append(time)
    crew.sort()
    ans = ''
    if len(crew) >= m:
        last_crew = crew[-1]
        hour, min = map(int, last_crew.split(':'))
        if min == 0:
            hour -= 1
            min = 59
        else:
            min -= 1
        str_hour = '0' + str(hour) if hour < 10 else str(hour)
        str_min = '0' + str(min) if min < 10 else str(min)
        ans = str_hour + ':' + str_min
    else:
        ans = last_bus
    return ans

print(solution(10, 25, 1, ["09:00", "09:10", "09:20", "09:30", "09:40" ,"09:50", "10:00", "10:10", "10:20", "10:30", "10:40", "10:50"]))