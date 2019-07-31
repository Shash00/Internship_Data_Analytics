import sqlite3
from prettytable import PrettyTable

host_name = "data.db"

def createdb():
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("create table student(regno integer primary key,name text,sem integter,placed integer)")
    except Exception as e:
        print(e)
    finally:
        conn.close()


def add_new_student(regno,name,sem,placed):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("insert into student (regno,name,sem,placed) values(?,?,?,?)",(regno,name,sem,placed))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def show_students():
    try:
        t = PrettyTable(['USN','Name','Sem','Status'])
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("select regno,name,sem,placed from student")
        rows = cursor.fetchall()
        for row in rows:
            status = "Placed" if row[3] == 1 else "Not Placed"
            t.add_row([row[0],row[1],row[2],status])
        print(t)
        
    except Exception as e:
        print(e)
    finally:
        conn.close()

def update_student(regno,placed):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("update student set placed=? where regno =?",(placed,regno))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def search_students(regno):
    try:
        t = PrettyTable(['USN','Name','Sem','Status'])
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("select regno,name,sem,placed from student where regno = ?",(regno,))
        rows = cursor.fetchall()
        for row in rows:
            status = "Placed" if row[3] == 1 else "Not Placed"
            t.add_row([row[0],row[1],row[2],status])
        print(t)
        
    except Exception as e:
        print(e)
    finally:
        conn.close()

add_new_student(1002,"Shash",7,0)
add_new_student(1003,"abc",8,1)
update_student(1002,1)
show_students()
search_students(1001)