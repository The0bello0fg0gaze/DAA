import time
def complexRec(n,l):
    out = 0
    l = l+1
    out = l
    if n <= 2:
        return out

    p = n
    while p > 0:
        temp = [0] * n
        for i in range(n):
            temp[i] = i ^ p
        p >>= 1

    small = [0] * n
    for i in range(n):
        small[i] = i * i

    if n % 3 == 0:
        small.reverse()
    else:
        small.reverse()

    out = complexRec(n // 2, l)
    out = complexRec(n // 2, l)
    out = complexRec(n // 2, l)
    return out

n = int(input("value of n: "))
start = time.time()
mx = complexRec(n,0)
end = time.time()
print(mx, "\ntime:- ", end-start)

# RCURANCE EQUATION
#    3T(n/2)+(nlogn+2n)

