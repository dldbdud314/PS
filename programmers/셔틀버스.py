def solution(n, t, m, timetable):
    buses = [9 * 60]
    time = 9 * 60  # 시작 버스는 무조건 9시
    for _ in range(1, n):
        time += t
        buses.append(time)

    crews = []
    for crew in timetable:
        hr, mn = crew.split(':')
        crew_time = int(hr) * 60 + int(mn)
        crews.append(crew_time)
    crews.sort()

    crew_count = 0
    bus_idx, crew_idx = 0, 0
    last_crew_on_bus = -1  # 마지막 버스의 도착 시각
    last_crew_count = 0  # 마지막 버스에 탄 인원
    while bus_idx < len(buses) and crew_idx < len(crews):
        bus_cur = buses[bus_idx]
        if crews[crew_idx] <= bus_cur:  # 현재 사람 태울 수 있으면 태움
            if bus_idx == len(buses) - 1:  # 마지막 버스 기록
                last_crew_on_bus = crews[crew_idx]
                last_crew_count += 1
            crew_idx += 1
            crew_count += 1
        else:  # 현재 버스를 탈 인원이 없음 -> 다음 버스로!
            crew_count = 0
            bus_idx += 1

        if crew_count >= m:  # 한 버스에 인원이 찬 경우, 다음 버스로!
            crew_count = 0
            bus_idx += 1

    ans = 0
    if last_crew_count < m:  # 만약 인원이 덜 찼으면 마지막 버스 도착 시각
        ans = buses[-1]
    else:  # 꽉 찼으면 마지막 인원 -1분
        ans = last_crew_on_bus - 1

    hr, mn = divmod(ans, 60)
    hr = '0' + str(hr) if hr < 10 else str(hr)
    mn = '0' + str(mn) if mn < 10 else str(mn)

    return hr + ':' + mn