from emp import Employee

lst_emp = []


def load_emp():
    with open('emp.txt') as f:
        data = f.readlines()
        for l in data:
            lst = l.strip('\n').split(',')
            eid = lst[0]
            name = lst[1]
            qual = lst[2]
            sal = lst[3]
            dept = lst[4]
            emp1 = Employee(eid, name, qual, sal, dept)
            lst_emp.append(emp1)
        print(len(lst_emp))


load_emp()
