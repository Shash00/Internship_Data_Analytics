import json
d = [{'id':1001,'Name':'Python','Status':'01'}, {'id':1002,'Name':'Java','Status':'00'}]

with open('ws.json','w') as f:
    json.dump(d,f,indent=2)
    print(json.dumps(d,indent=2))