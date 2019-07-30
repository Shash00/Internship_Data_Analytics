import json
def add_ws(lst):
    with open('ws.json','w') as f:
        json.dump(lst,f,indent=2)
        
def add_stu(lst):
    with open('stu.json','w') as f:
        json.dump(lst,f,indent=2)
        
def display():
    with open('ws.json','r') as w, open('stu.json','r') as r:
        s_lst = json.load(r)
        w_lst = json.load(w)

    for s in s_lst:
        for w in w_lst:
            if s["cid"] == w["id"]:
                print(f'{s["cid"]},{s["name"]}')

if __name__ == "__main__":
    while True:
        print('Enter your choice: 1.Add Course 2.Add student 3.Display 4.Exit')
        ch = int(input('Choice:'))
        if ch == 1:
            lst = [i for i in dict(map(str,input("Id, Name, Status: ").split(',')))]
            add_ws(lst)
        elif ch == 2:
            lst = [i for i in dict(map(str,input("Regno, Name, Cid: ").split(',')))]
            add_stu(lst)
        elif ch == 3:
            display()
        elif ch == 4:
            break
