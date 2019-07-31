import time
import random as rn
import dbcontext as db
from models import Internship 
from beautifultable import BeautifulTable
from prettytable import PrettyTable

def _get_new_id():
    t_obj = time.localtime()
    new_id = rn.randint(1000,9900) + (t_obj.tm_min + t_obj.tm_hour + t_obj.tm_sec)
    return new_id

def add_internship(iname,company,i_year):
    id = _get_new_id()
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into internship(id,iname,company,i_year,status) values(?,?,?,?,?)",(id,iname,company,i_year,1))
            print(f"Internship is added successfully with id:{id}")
    except Exception as e:
        print(str(e))

def view_all_internships():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select id,iname,company,i_year,status from internship")
            rows = cursor.fetchall()
            intern_pro_lst = [Internship(*row) for row in rows]
            _view_internship_list(intern_pro_lst)
    except Exception as e:
        print(str(e))

def search_internship_by_name(name):
    try:
        t = PrettyTable(['ID','Name','Company','Year','Status'])
        with db.DbContext() as conn:
            cursor = conn.cursor()
            cursor.execute("select id,iname,company,i_year,status from internship where iname = ?",(name,))
            rows = cursor.fetchall()
            for row in rows:
                t.add_row([row[0],row[1],row[2],row[3],row[4]])
            print(t)
    except Exception as e:
        print(e)


def change_status_internship(status,name):
    try:
        with db.DbContext() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE internship set status = ? where iname = ? ", (status,name))
            conn.commit()
    except Exception as e:
        print(e)


def delete_internship(id):
    try:
        with db.DbContext() as conn:
            cursor = conn.cursor()
            cursor.execute("Delete from internship where id = ?", (id,))
    except Exception as e:
        print(e)


def add_student(usn,name,sem,placed):
    try:
        with db.DbContext() as conn:
            cursor = conn.cursor()
            cursor.execute("insert into student(usn,name,sem,placed) values(?,?,?,?)",(usn,name,sem,placed))
            print(f"Registration is successfull")
    
    except Exception as e:
        print(e)

def view_students():
    try:
        t = PrettyTable(['USN','Name','Sem','Placed'])
        with db.DbContext() as  conn:
            cursor = conn.cursor()
            cursor.execute("select usn,name,sem,placed from student")
            rows = cursor.fetchall()
            for row in rows:
                t.add_row(row)
            print(t)
    except Exception as e:
        print(e)


def search_student_by_name(name):
    try:
        t = PrettyTable(['USN','Name','Sem','Placed'])
        with db.DbContext() as conn:
            cursor = conn.cursor()
            cursor.execute("select usn,name,sem,placed from student where name = ?",(name,))
            rows = cursor.fetchall()
            for row in rows:
                t.add_row(row)
            print(t)

    except Exception as e:
        print(e)


def update_student(usn,sem):
    try:
        with db.DbContext() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE student set sem = ? where usn = ?",(sem,usn))
            print("Student successfully updated")

    except Exception as e:
        print(e)


def delete_student(usn):
    try:
        with db.DbContext() as conn:
            cursor = conn.cursor()
            cursor.execute("Delete from student where usn = ?",(usn,))
            print("Successfully deleted")
    
    except Exception as e:
        print(e)

def add_student_internship(iid,usn,status):
    try:
        with db.DbContext() as conn:
            cursor = conn.cursor()
            cursor.execute("insert into regi values(iid,usn,status)",(iid,usn,status))

    except Exception as e:
        print(e)

def view_all_reg_student():
    pass

def company_ws_count():
    pass
def student_ws_count():
    pass
def ws_student_reports():
    pass

def reg_stu_internship():
    pass

def update_stu_intership_status():
    pass


def _view_internship_list(lst):
    if lst and len(lst) > 0:
        table = BeautifulTable()
        table.column_headers = ["ID", "NAME", "COMPANAY", "YEAR","STATUS"]
        for l in lst:
            status = "Comleted" if l.status == 0 else "Going on" 
            table.append_row([l.id, l.iname, l.company, l.i_year,status])
        print(table)
    else:
        print(f"There are no Intership programms, yet to add...")