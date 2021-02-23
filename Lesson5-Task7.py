import codecs
import json

def getData():
    ret = {}
    with codecs.open( "companies.txt", "r", "utf_8_sig" ) as f:
        for line in f:
            if not line.strip():
                continue
            data = line.split()
            ret[data[0]] = { 'type': data[1], 'income': int(data[2]), 'expense': int(data[3]) }
    return ret

avg = 0
count = 0
companies = getData()
ret = [{}, { 'Average': 0 }]
for company, data in companies.items():
    data['total'] = data['income'] - data['expense']
    if data['total'] > 0:
        avg += data['total']
        count += 1
    ret[0][company] = data['total']
    if count > 0:
        ret[1]['Average'] = avg / count
print(ret)
with open('result.json', 'w') as f:
    json.dump(ret, f)