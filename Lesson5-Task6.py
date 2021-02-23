import codecs
ret = {}

def split(txt, seps):
    default_sep = seps[0]
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    ret = txt.split(default_sep)
    while '' in ret:
        ret.remove('')
    return ret

with codecs.open( "dict.txt", "r", "utf_8_sig" ) as f:
    for line in f:
        if not line.strip():
            continue
        values = split(line, ['(л)','(пр)','(лаб)','.',':',' '])
        ret[values[0]] = sum([int(item) for item in values[1:] if item.isdigit()])
    print(ret)