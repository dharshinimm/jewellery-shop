#!c:\Python312\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

form=cgi.FieldStorage()
fname=form.getvalue("name")
fcountry=form.getvalue("country")
fstate=form.getvalue("state")
fnumber=form.getvalue("number")
ffund=form.getvalue("fund")
fjewelltype=form.getvalue("jewelltype")
fpincode=form.getvalue("pincode")


print(fname,fcountry,fstate,fnumber,ffund,fjewelltype,fpincode)


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bluestone",


)
mycursor=mydb.cursor()

sql="INSERT INTO jewellery(Name,Country,State,Number,Fund,Jewelltype,Pincode)VALUES(%s,%s,%s,%s,%s,%s,%s)"
val=(fname,fcountry,fstate,fnumber,ffund,fjewelltype,fpincode)

mycursor.execute(sql,val)
mydb.commit()


