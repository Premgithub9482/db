import mysql.connector as m

con_obj=m.connect(user='root',password='Prem@9482',host='localhost',database='demo')
cur_obj=con_obj.cursor()

def saltab():
    try:
        qry="create table salary(Ecode varchar(15), Name varchar(25), Year Varchar(20), month varchar(20), Working_days integer, Finalpay integer)"
        cur_obj.execute(qry)
    except:
        print('Table already exist')
saltab()

def showtab():
    qry='desc salary'
    cur_obj.execute(qry)
    for i in cur_obj:
        print(i)
showtab()

def saldata():
    try:
        qry="insert into salary values(%s,%s,%s,%s,%s,%s)"
        ec=input('Enter employee code: ')
        n=input("Enter employee Name:" )
        y=input('Enter year: ')
        m=input('Enter month: ')
        wd=int(input('Enter working days: '))
        fp=int(input('Enter final pay: '))
        data=(ec,n,y,m,wd,fp)
        cur_obj.execute(qry,data)
    except:
        print('Some error occured')
    else:
        print('Data saved successfully')
        cur_obj.execute('select * from salary')
        for i in cur_obj:
            print(i)
saldata()