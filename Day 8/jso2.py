import json

with open('ws.json','r') as w, open('stu.json','r') as r:
    s_lst = json.load(r)
    w_lst = json.load(w)

for s in s_lst:
    for w in w_lst:
        if s["cid"] == w["id"]:
            print(f'{s["cid"]},{s["name"]}')