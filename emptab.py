import mysql.connector as m

con_obj=m.connect(user='root',host='localhost',password='Prem@9482',database='demo')
cur_obj=con_obj.cursor()

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
