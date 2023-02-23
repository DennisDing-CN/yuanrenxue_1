import execjs
import time
import requests

with open('2.js', 'r', encoding='utf-8') as f:
    line = execjs.compile(f.read())
total = 0
times = 0
for i in range(1, 6):
    t = int(time.time()) * 1000 + 100000000
    mm = line.call('get_m',str(t))
    params = {
        'page': i,
        'm': str(mm) + '丨' + str(int(t/1000)),
    }
    headers = {
        'user-agent': 'yuanrenxue.project',
        'cookie': 'sessionid=q1axbzfiaiofuonfslwm0p88z3c159fo;',
    }
    response = requests.get('https://match.yuanrenxue.com/api/match/1', headers=headers, params=params)
    print(response.text)
    data = response.json()["data"]
    times += len(data)
    for d in data:
        total += d["value"]

print(int(total / times))