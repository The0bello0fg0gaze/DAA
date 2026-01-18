class Link:
    def __init__(self,cost=None ,val=None, left=None, right=None):
        self.cost = cost
        self.val = val
        self.left = left
        self.right = right
    def show(self,n):
        n += 1
        if self.left:
            print("-l"*n,self.left.val)
            self.left.show(n)
        if self.right:
            print("-r"*n, self.right.val)
            self.right.show(n)
        return 0

def rep(data):
    out = {}
    for x in set(data):
        out[x] = 0
    for x in data:
        out[x] += 1
    out = sorted(out.items(), key=lambda items: items[1], reverse= True)
    ret = []
    for x in out:
        ret += [Link(x[1],x[0])]
    return ret

def huffman(data):
    while len(data)>1:
        sm = data[0].cost + data[1].cost
        data += [Link(sm,'#',data.pop(0),data.pop(0))]
    return data

data = rep("hell")
root = huffman(data)[0]
root.show(1)
