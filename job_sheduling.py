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
jobs = [ ['J1',100,2], ['J2',19,1], ['J3',87,2], ['J4',25,1], ['J5',15,1]]
print(jobsheduling(2, jobs))
