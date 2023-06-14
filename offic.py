import mysql.connector as m

con_obj=m.connect(user='root',host='localhost',password='Prem@9482',database='demo')
cur_obj=con_obj.cursor()
def Officetab():
    try:
        qry='create table office(Ecode varchar(15), EName varchar(25),Post varchar(25),joining varchar(10),BasicPay integer)'
        # cur_obj=con_obj.cursor()
        cur_obj.execute(qry)
    except:
        con_obj.rollback()
        print('table already created')
Officetab()
