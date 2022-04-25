from collections import defaultdict

def calc_time(in_time, out_time):
    in_hr, in_min = int(in_time[0]), int(in_time[1])
    out_hr, out_min = int(out_time[0]), int(out_time[1])
    return (out_hr * 60 + out_min) - (in_hr * 60 + in_min)

def calc_fee(default_time, default_fee, per_time, per_fee, cur_time):
    if cur_time <= default_time:
        return default_fee
    else:
        etc_time = 0
        if (cur_time-default_time) % per_time == 0: etc_time = (cur_time-default_time) // per_time
        else: etc_time = (cur_time-default_time) // per_time + 1
        return default_fee + etc_time * per_fee

def solution(fees, records):
    record_dict = defaultdict(list)
    times_dict = defaultdict(int)
    for record in records:
        time, num, status = record.split()
        if status == 'IN': record_dict[num].append(tuple(time.split(":")))
        else: times_dict[num] += calc_time(record_dict[num].pop(), tuple(time.split(":")))
    for key, val in record_dict.items(): #in만 있고 out이 없는 경우
        if val: 
            times_dict[key] += calc_time(val.pop(), ('23', '59'))
    fees_dict = defaultdict(int)
    for key, value in times_dict.items():
        fees_dict[key] += calc_fee(fees[0], fees[1], fees[2], fees[3], value)
    fees_dict = sorted(fees_dict.items(), key = lambda x:x[0])
    
    return list(map(lambda x : x[1], fees_dict))