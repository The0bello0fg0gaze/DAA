def rep(data):
    out = {}
    for x in set(data):
        out[x] = 0
    for x in data:
        out[x] += 1
    return sorted(out.items(), key=lambda items: items[1], reverse= True)

def huffman(queue):
    return 0   

print(rep("hello"))
