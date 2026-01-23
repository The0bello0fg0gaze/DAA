weights = [ [10,110], [30,40], [20,60] ]

def Ratio(d):
    return (d[1]/d[0])

def napsac(weights, capacity):
    ratio = sorted(weights, key=Ratio)
    out = 0
    for x in ratio:
        if capacity > x[0]:
            capacity -= x[0]
            out += x[1]
        else:
            out += (x[1]/x[0])*capacity
    return out

print(napsac(weights,60))



