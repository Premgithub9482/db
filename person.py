import mysql.connector as m

con_obj=m.connect(user='root',password='Prem@9482',host='localhost',database='demo')
cur_obj=con_obj.cursor()

def persontab():
    qry='create table personal(Name varchar(25), City varchar(25), D_O_B varchar(20), Phone varchar(15))'
    try:
        cur_obj.execute(qry)
    except:
        print('table already exist')
    else:
        print('Table created successfully')
        qry='select * from personal'
        cur_obj.execute(qry)
persontab()

def persondata():
    try:
        qry="insert into personal values(%s,%s,%s,%s)"
        n=input('Enter Name: ')
        c=input('Enter City Name: ')
        db=input('Enter Birth Date: ')
        p=int(input('Enter phone number: '))
        data=(n,c,db,p)
        cur_obj.execute(qry,data)
    except:
        print('Some Error Occured')
    else:
        print('Data Entered Successfully')
        cur_obj.execute('select * from personal')
        for i in cur_obj:
            print(i)
persondata()