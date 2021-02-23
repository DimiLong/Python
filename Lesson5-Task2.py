with open('text.txt') as f:
    ret = []
    idx = 1
    for line in f:
        ret.append({ "row": idx, "num of words": len(line.split()) })
print (ret)