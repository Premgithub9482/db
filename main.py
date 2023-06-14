import mysql.connector as m

con_obj=m.connect(user='root',password='Prem@9482',host='localhost',database='demo')
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
    main()

def emp():
    qry='select * from emp'
    cur_obj.execute(qry)
    data=cur_obj.fetchall()  # or data=cur_obj
    for i in data:
        print(i)
    main()

def officedata():
    try:
        ec=int(input('Emp code: '))
        en=input('Enter Employees Name: ')
        p=input('Enter Employees Post: ')
        jd=input('Enter employees joining date: ')
        bp=int(input('Enter Employees Assigned salary: '))
        data=(ec,en,p,jd,bp)
        qry="insert into office values(%s,%s,%s,%s,%s)"
        cur_obj.execute(qry,data)
        con_obj.commit()
        print('Data Entered Successfully')
    except:
        print('Some Error occured')
    main()

def office_show():
    try:
        qry='select * from office'
        cur_obj.execute(qry)
        d=cur_obj.fetchall()
    except:
        print('Some Error Occured')
    else:
        for i in d:
            print(i)
    main()

def nsalary():
    # global v,bs
    # ec=input('Enter Employee code: ')
    # v=(ec,)
    # qry='select basicpay from office where Ecode=%s'
    # cur_obj.execute(qry,v)
    # bs=cur_obj.fetchone()
    # print('Data Entered Successfully')
    try:
        ec=input('Enter Employee code: ')
        v=(ec,)
        qry='select basicpay from office where Ecode=%s'
        cur_obj.execute(qry,v)
        bs=cur_obj.fetchone()
        n=input('Enter EMployee Name: ')
        y=input('Enter year: ')
        m=input('Enter Month: ')
        wd=int(input('Enter working days: '))
        td=int(input('Enter total days: '))
        fp=bs[0]/(td*wd) 
        data=(ec,n,y,m,wd,fp)
        qry='insert into salary values(%s,%s,%s,%s,%s,%s)'
        cur_obj.execute(qry,data)
        con_obj.commit()
        print('Data Entered Successfully')
    except:
        print('SomeError')
    main()

def saltab():
    qry='select * from salary'
    cur_obj.execute(qry)
    data=cur_obj.fetchall()
    for i in data:
        print(i)
    main()

def main():
    print('''
    1. Add New Employee Personal Details
    2. Display Employees Personal Details
    3. Add New Employee Office Details
    4. Display Employees Office Details
    5. Enter Salary Details Of Employee
    6. Display Salary Details of Employee
    9. To Quit Enter 9
    ''')
    choice=int(input('Enter task: '))
    while True:
        if choice==1:
            empinfo()
        elif choice==2:
            emp()
        elif choice==3:
            officedata()
        elif choice==4:
            office_show()
        elif choice==5:
            nsalary()
        elif choice==6:
            saltab()
        elif choice==9:
            quit()
        else:
            print('Choose the correct choice')
            break
main()