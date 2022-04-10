def solution(id_list, report, k):
    report_dict = {id : list() for id in id_list}
    record = {id : 0 for id in id_list}
    for x in report:
        x_list = x.split()
        if x_list[1] not in report_dict[x_list[0]]:
            report_dict[x_list[0]].append(x_list[1]) 
            record[x_list[1]] += 1
    
    report_list = []
    for id in id_list:
        report_list.append(report_dict[id])
    
    ans = []
    for a in report_list:
        num = 0
        for aa in a:
            if record[aa] >= k: num += 1
        ans.append(num)
    return ans
