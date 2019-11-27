# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import mysql.connector
'''
#-------------------------FIRST SQL CLASS(ORACLE)----------------------------------------------------------
==>A schema  is a collection of database object for a particular user  e.g tables ,views
every relationmship for a table is always one to many
primary identification  for the table  (primary key)
anything with attributes is an entry
1-many relationship
1-1 relationship
many-many relationship
1-many or many-1 is normalised
SELECT is to view info on the Database
## DISTINCT is to show everything unique that is no repetition
select  distinct salary SAL from employees
select  salary SAL from employees == alias
select  4*4 from employees == expression
select  first_name || ' ' || last_name Fullname salary " monthly salary ", salary*12  " annual salary " from employees; == string(string) and arithmetic operator
select  first_name ||' '|| last_name "Full_Name",  salary,  salary*1.5 " revised salary " from employees;
select  first_name  salary  from employees where salary >= 10000;
select  first_name  salary  from employees where salary >= 3000;
select  first_name,hire_date  salary  from employees where salary >= 3000 and hire_date >= '01-JAN-80';

select * from employees where employee_id <> 120
select * from employees where employee_id BETWEEN 100 AND 102
select * from employees where employee_id IN (115,114,120)
select * from employees where commission_pct IS NULL
select * from employees where employee_id in (120,121) and commission_pct IS NULL
select * from employees where employee_id not in (120,121) and commission_pct IS NULL

WILDCARD CHARACTER
select * from employees where first_name like 'st%'
select * from employees where first_name like '%a%'
select * from employees where first_name like '%a_' == ends with one character after
select * from employees where first_name like '_a_' == ends with one character after and before

RULES OF PRECEDENCE
Arithmetic operators
concatenation operator
Comparison conditions
IS [NOT] NULL ,LIKE,[NOT] IN
[NOT] BETWEEN
Not equal to
NOT logic condition
AND logical condition
OR logical condition

USING ORDER BY CLAUSE()
select * from employees order by first_name
select * from employees order by first_name desc;
select department_id,first_name,last_name from employees order by department_id,first_name
select department_id,first_name,last_name from employees order by 1,2


SQL FUNCTIONS:multi-row and single-row
singlerow: works on each row  e.g upper[multiple argument] one result per role
multirow:collection of row e.g sum[single arguments] one result per set of roles

NUMBER:sum(salary),avg,abs,rand,div,floor,greatest(age,30)==returns ageonly when its >30,least,pow(salary,2)==salary**2,trunc
>select salary,mod(salary,3) from employees

DATE:add_months(sysdate,3),last_day()==returns last day,months_between(sysdate,hire_date)==specifies ,next_day(),round(),sysdate()==gives current date,trunc()
rr-2017 yy-1917
                 RR 0-49                                                YY  50-99
RR 0-49  return date is in the current century                   the return date is in the century before the current one
YY 50-99 return the date in the century after the current one    returns the date in the current one
#dual=pseudocolumn
>select sysdate from dual
>select concat('todays date is',sysdate) from dual
>select 'todays date is' || sysdate from dual

CHARACTER(Case and Character):when the func works on char or strings e.g upper,lower,initcap(capitalises the initials),lpad{formatting(salary,1[number of times],'N')},rpad
length,substring(first_name,1{first name on list},3{remove first 3 char}),instr(first_name,'a')==returns where the  position of 'a' is,replace(value,replace as),TRIM('H',from,'HELLO WORLD')
case> select department_id,upper(first_name) firstname,lower(last_name ) lastname from employees order by 1,2
char> select department_id,upper(first_name) firstname,lower(substr(last_name,1,3) ) lastname from employees order by 1,2
char> select department_id,upper(first_name) firstname, concat('Hello ' , lpad(lower(substr(last_name,1,3)),5,'#' )) lastname from employees order by 1,2

CONVERSION FUNCTIONS and conditional exp:implicit and explicit
conv by database itself is implicit(varchar/char-date or char/varchar-num)
conv by programmer is explicit
NUM =CHAR =DATE
TO_CHAR(date, 'format_model')
select employee_id , TO_CHAR(hire_date, 'DD/MM/YY') as "Employment date" from employees
select employee_id , TO_CHAR(hire_date, 'ddspth "of" Mon YYYY') as "Employment date" from employees
select first_name, to_char(salary,'L99,999,999.00') as "currency" from employees
select first_name,salary,commission_pct, salary+commission_pct from employees == wrong
select first_name,salary,commission_pct, salary+nvl(commission_pct,0) from employees == correct (nvl=null value)

GENERAL FUNCTIONS:
    
    
    
#----------------------------FIRST SQL+PROGRAMMING CLASS(XAMPP)----------------------------------------
#To create Database
mycon = mysql.connector.connect(host='localhost or 127.0.0.1',user= 'root',password='')
mycursor= mycon.cursor()
mycursor.execute('CREATE DATABASE cbt_db')
#-----------------------------------------------------------------------------------------------------------
#To Alter a database(change)
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='cbt_db')
mycursor= mycon.cursor()
mycursor.execute('ALTER TABLES registration CHANGE reg_id reg_idINT(4) PRIMARY KEY AUTO_INCREMENT')
#-----------------------------------------------------------------------------------------------------------
#To Alter a database(drop)
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='cbt_db')
mycursor= mycon.cursor()
mycursor.execute('ALTER TABLES registration DROP password')
mycon.commit()
#-------------------------------------------------------------------------
#To Alter a database(add)
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='cbt_db')
mycursor= mycon.cursor()
mycursor.execute('ALTER TABLES registration ADD password VARCHAR(20)')
mycon.commit()
#To crteate Table
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='cbt_db')
mycursor= mycon.cursor()
mycursor.execute('CREATE TABLE registration (reg_id INT(4), user_name VARCHAR(60), password VARCHAR(30))')
mycon.commit()
#-------------------------------------------------------------------------------
##Before insertion,set key to primary and auto-increase##
#To insert inside the database Table
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='cbt_db')
mycursor= mycon.cursor()
##in order to avoid sql ejection we put them in variables##
sql = 'INSERT INTO registration(user_name,password) VALUES(%s,%s)'
val = [('Michael','top123'),('Tomisin','me234'),('Dolapo','Dollyp1234'),('Gbemileke','lekestar2000')]
mycursor.executemany(sql,val)
mycon.commit()
print(mycursor.rowcount,'Record Inserted successfully')
#--------------------------------------------------------------------------------------------
#To Select(print) from database
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='cbt_db')
mycursor= mycon.cursor()
mycursor.execute('SELECT * FROM registration')
##or('SELECT password,username FROM registration')## myreg = mycursor.fetchone()##
##or('SELECT password,username FROM registration WHERE reg_id = 4')## myreg = mycursor.fetchone()##
##or("SELECT password,username FROM registration WHERE username like '%what we are looking for'")## myreg = mycursor.fetchonel()##
## or('SELECT * FROM registration ORDER BY reg_id DESC')
myreg = mycursor.fetchall()
for info in myreg:
    print(info)
mycon.commit()
print(mycursor.rowcount,'record received successfully')
#-------------------------------------------------------------------------------------------
#To Delete from a database
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='cbt_db')
mycursor= mycon.cursor()
sql = 'DELETE FROM registration username =%s'
val = ('olu8')
mycursor.execute(sql,val)
mycon.commit()
print(mycursor.rowcount,'deleted successfully')
#------------------------------------------------------------------------------------------------
#To Update a database
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='cbt_db')
mycursor= mycon.cursor()
sql = 'UPDATE registration SET  username =olu WHERE username=%s'
val = ('olu8')
mycursor.execute(sql,val)
mycon.commit()
print(mycursor.rowcount,'updated successfully')
#---------------------------------------------------------------------------------------------------
#Setting limit to a a database(first set of values or last set of values)
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='cbt_db')
mycursor= mycon.cursor()
query = 'SELECT * FROM username LIMIT 6' OR 'SELECT * FROM username LIMIT 6 OFFSET 6'##in-between selections
mycursor.execute(query)
myreg = mycursor.fetchall()
for info in myreg:
    print(info)
mycon.commit()
print(mycursor.rowcount,'selected successfully')
#---------------------------------------------------------------------------------------
#Joining two tables in a databse
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='cbt_db')
mycursor= mycon.cursor()
query = 'SELECT * FROM username, password FROM registration JOIN SecondTable USING reg_id'
myreg = mycursor.fetchall()
for info in myreg:
    print(info)
mycon.commit()
print(mycursor.rowcount,'selected successfully')
'''

