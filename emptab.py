import mysql.connector as m

con_obj = m.connect(user='root', host='localhost', password='Prem@9482', database='demo', auth_plugin='mysql_native_password')
cur_obj=con_obj.cursor()


def emp_tab():
    qry='create table emp(Name varchar(25), City varchar(25), D_O_B varchar(20), Phone varchar(15))'
    try:
        cur_obj.execute(qry)
    except:
        print('table already exist')
    else:
        print('Table created successfully')
        qry='select * from emp'
        cur_obj.execute(qry)
emp_tab()

def empinfo():
    try:
        n=input('Enter Employee Name: ')
        c=input('Enter Employee City Name: ')
        d=input('Enter Employee D-O-B: ')
        p=input('Enter Employee Phone: ')
        data=(n,c,d,p)
        query='insert into emp values(%s,%s,%s,%s)'
        cur_obj.execute(query,data)
        con_obj.commit()
        print('data entered successfully')
    except:
        con_obj.rollback()
        print('some error occured')
empinfo()

def emp():
    qry='select * from emp'
    cur_obj.execute(qry)
    data=cur_obj.fetchall()  # or data=cur_obj
    for i in data:
        print(i)
emp()
