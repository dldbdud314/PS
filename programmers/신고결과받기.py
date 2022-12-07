def solution(id_list, report, k):
    reported_id = {user_id: 0 for user_id in id_list}  # 누가 신고 몇 회 당했는지
    report_stat = {user_id: list() for user_id in id_list}  # 누굴 신고했는지 저장

    for x in set(report):
        reporter, reported = x.split()
        reported_id[reported] += 1
        report_stat[reporter].append(reported)

    suspended_ids = set()
    for user_id, count in reported_id.items():
        if count >= k:
            suspended_ids.add(user_id)

    res = [0] * len(id_list)
    i = 0
    for user_id, reported_list in report_stat.items():
        for reported in reported_list:
            if reported in suspended_ids:
                res[i] += 1
        i += 1

    return res
