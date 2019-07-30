import csv

d = [{'id':1001,'Name':'Python','Status':'01'}]
try:
    with open('cs.csv','w',newline='') as f:
        header = ['id','Name','Status']
        writer = csv.DictWriter(f,fieldnames=header)
        # writer.writeheader()
        writer.writerows(d)
except Exception as e:
    print(e)