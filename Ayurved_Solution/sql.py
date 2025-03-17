from re import S
from unicodedata import category
# import pymysql as p
import sqlite3
 
def getconnection():
   
    return sqlite3.connect("ayurveda.db")
 
 
#insert record
def insertrec(t):
    db=getconnection()
    cr=db.cursor()
    sql="insert into medicine (id, category, problem, details, image, link) VALUES (?, ?, ?, ?, ?, ?)"
    cr.execute(sql,t)
    print(t)
    db.commit()
    db.close()
#edit record
def updaterec(t):
    db=getconnection()
    cr=db.cursor()
    sql="UPDATE medicine SET category=?, problem=?, details=?, image=?, link=? WHERE id=?"
    cr.execute(sql,t[:6])
    db.commit()
    db.close()
 
 
#display record
def displayrec():
    db=getconnection()
    cr=db.cursor()
    sql="select * from medicine"
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
 
#delete record 
def deleterec(id):
    db=getconnection()
    cr=db.cursor()
    sql="delete from medicine where id=?"
    cr.execute(sql,(id,))
    db.commit()
    db.close()
 
 
 
#select record
def selectr(id):
    db=getconnection()
    cr=db.cursor()
    sql="select * from medicine where id=?"
    cr.execute(sql,id)
    data=cr.fetchall()
    print(data)
    db.commit()
    db.close()
    return data[0]


#display category
def displayrec1(category):
    db=getconnection()
    cr=db.cursor()
    sql="select * from medicine where category=?"
    cr.execute(sql, (category,))
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
