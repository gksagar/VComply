def availableLeaveSlots(approvedLeaves,startDate,endDate):
    s = startDate.split('-')
    start = date(s[2],s[1],s[0])
    e = startDate.split('-')
    end = date(e[2],e[1],e[0])
    ans = []
    for d in approvedLeaves:
        d1 = d[leaveFrom]
        d2 = d[leaveUpto]
        day1 = date(d1[2],d1[1],d1[0])
        day2 = date(d2[2],d2[1],d2[0])
        if day1>=start and day2<=end:
            dic = {}
            dic['availableFrom'] = d[leaveFrom]
            dic['availableUpto'] = d[leaveUpto]
            ans.append(dic)
    return ans
        
        
