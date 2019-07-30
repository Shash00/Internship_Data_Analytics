import json

with open('ws.json','r') as f:
    lst = json.load(f)
    for i in lst:
        print(f"Id:{i['id']},Name:{i['Name']}")