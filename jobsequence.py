def jobsheduling(n,jobs):
    slots = [0]*n
    jobs = sorted(jobs, key=lambda job: job[1], reverse=True)
    for job, cost, d in jobs:
        while d-1 >= 0 and d-1 < n:
            if slots[d-1] == 0:
                slots[d-1] = cost
                break
            else:
                d -= 1
    return slots
    
print(jobsheduling(2, [['J1',100,1],['J2',120,3],['J3',40,2]]))
