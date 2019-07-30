d = [{'id':1001,'Name':'Python','Status':'01'}]

try:
    with open ('dat1.txt','w') as f:
            line = f'{d["id"]},{d["Name"]},{d["Status"]}\n'
            f.write(line)

except Exception as e:
    print(f"{e}")