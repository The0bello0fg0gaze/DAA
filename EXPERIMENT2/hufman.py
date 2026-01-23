class heap():
    def __init__ (self, cost=0, val='#',left=None, right=None):
        self.cost = cost
        self.val = val
        self.left = left
        self.right = right

class enc():
    def __init__(self):
        self.dct = {}
    def encode(self, root, out):
        if root.left:
            out += self.encode(root.left,out)+'0'
        else:
            self.dct[root.val] = out + '0'
        if root.right:
            out += self.encode(root.right, out)+'1'
        else:
            self.dct[root.val] = out + '1'
        return out

def hufman(lst):
    while len(lst) > 1:
        temp = heap()
        temp.left = lst.pop(0)
        temp.right = lst.pop(0)
        lst += [temp]
    return lst[0]

def unique(word):
    out = []
    for x in set(word):
        out += [heap(word.count(x),x)]
    return sorted(out, key=lambda x: x.cost, reverse= True)

i = input("words to enter:- ")
lst = unique(i)
print(lst)
tree = hufman(lst)
print(tree)
ed = enc()
ed.encode(tree,'')

print(ed.dct)






