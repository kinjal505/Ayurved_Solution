from os import link
import os
from re import U
from tkinter import Image
from unicodedata import category
from flask import *
from sql import *

app=Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "pushpa_lamboo")

#home page
@app.route("/")
def home():
  return render_template("home.html")


#admin  page
@app.route("/admin")
def mainlog():
  return render_template("admin.html")
 

#login page
@app.route("/login")
def login():
  return render_template("login.html")

#logout
@app.route("/logout")
def logout():
  return redirect("/")

#ERROR page
@app.route("/ERROR")
def ERROR():
  return render_template("ERROR.html")

#validating login
@app.route("/mainlogin" )
def adm():
  username=request.args.get("username")
  password=request.args.get("password")
  if (username=='kinjal' and password=='123'):
    return render_template("admin.html")
  else:
    return render_template("ERROR.HTML")

#adding values
@app.route("/adding")
def adding():
  return render_template("add.html")

#inserting values
@app.route("/insert",methods=["post"])
def insert():
  id=request.form["id"]
  category=request.form["category"]
  problem=request.form["problem"]
  details=request.form["details"]
  image=request.form["img"]
  link=request.form["link"]
  t=(id,category,problem,details,image,link)
  insertrec(t)
  return redirect("/")
 
 
#edit display data
@app.route("/details")
def details():
  x=displayrec()
  return render_template("details.html",elist=x)


#edit data
@app.route("/edit")
def edit():
  id1=request.args.get("id")
  y=selectr(id1)
  return render_template("edit.html",elist=y)

#update record
@app.route("/update",methods=["post"])
def update():
  id=request.form["id"]
  category=request.form["category"]
  problem=request.form["problem"]
  details=request.form["details"]
  image=request.form["img"]
  link=request.form["link"]
  t=(id,category,problem,details,image,link,id)
  updaterec(t)
  return redirect("/details")

#delete record
@app.route("/delete")
def delete():
  z=request.args.get("id")
  deleterec(z)
  return redirect("/details")

#user page
@app.route("/user")
def user():
  U=displayrec()
  print(U)
  return render_template("user.html", elist=U)

#category display
@app.route("/cate")
def usercategory():
  se=request.args.get("search")  
  c=displayrec1(se)
  return render_template("user.html",elist=c)
     
if __name__=="__main__":
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))  # Render assigns a PORT dynamically
    app.run(host="0.0.0.0", port=port)