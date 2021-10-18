import mysql.connector
import getpass
from tkinter import *
from tkinter import ttk
global cursor
global a_database_is_selected
a_database_is_selected=int(0)
def reset():
    username_input.set("")
    passname_input.set("")
def login():

    def addpass():
        viewframe=Tk()
        viewframe.geometry("350x200+0+0")
        webname=StringVar()
        username=StringVar()
        password=StringVar()
        Label(viewframe,text="Website:",fg="steel blue",font=('arial',12,'bold')).place(x=45,y=20)
        Label(viewframe,text="Username:",fg="steel blue",font=('arial',12,'bold')).place(x=45,y=55)
        Label(viewframe,text="Password:",fg="steel blue",font=('arial',12,'bold')).place(x=45,y=90)
        Entry(viewframe,textvariable=webname,font=('arial',10)).place(x=145,y=20)
        name=webname.get()
        webname.set(name)
        Entry(viewframe,textvariable=username,font=('arial',10)).place(x=145,y=55)
        name=username.get()
        username.set(name)
        Entry(viewframe,textvariable=password,font=('arial',10)).place(x=145,y=90)
        name=password.get()
        password.set(name)
        def addtodb():
            s1=str(webname.get())
            s2=str(username.get())
            s3=str(password.get())
            sql="INSERT INTO BILL (WEBSITE,USER_NAME,PASSWORDS) VALUES (%s,%s,%s)" % (s1,s2,s3)
            
            try:
                cursor.execute(sql)
                _connection.commit()
                """pop=Tk()
                pop.geometry("200x100+0+0")
                Label(pop,text="Success!!",fb="green",font=('arial',10,'bold')).grid(row=0,column=0)
                def desta():
                    pop.destroy()
                    viewframe.destroy()
                Button(pop,padx=4,pady=0,fb="black",font=('arial',10,'bold'),text="Done!",command=desta).grid(row=1,column=0)"""
            except :
                """pop=Tk()
                pop.geometry("200x100+0+0")
                Label(pop,text="Some Error occurred!!",fb="red",font=('arial',10,'bold')).grid(row=0,column=0)
                def desta():
                    pop.destroy()
                    viewframe.destroy()
                Button(pop,padx=4,pady=0,fb="black",font=('arial',10,'bold'),text="Close!!",command=desta).grid(row=1,column=0)"""
                print("error")
        Button(viewframe,padx=4,pady=0,fg="black",font=('arial',10,'bold'),text="Add Password",command=addtodb).place(x=160,y=125)
    def updatepass():
        pass
    def deletepass():
        pass

    host="localhost"
    name=str(username_input.get())
    passwd=str(passname_input.get())
    try:
        global _connection
        _connection = None
        if not _connection:
            _connection= mysql.connector.connect(
            host="localhost",
            user="DARKSHADOW26",
            passwd="9782132659a@A",
            buffered=True
            #user=name,
            #passwd=passwd
        )
        global cursor
        cursor=_connection.cursor()

        #*******************************NEW WINDOW****************************
        roo=Tk()
        roo.geometry("400x185+0+0")
        roo1=Frame(roo,width=500,height=165,relief=SUNKEN)
        roo1.pack(side=TOP)
        lab=Label(roo1,text="Available Options:",fg="green",font=('arial',15,'bold'))
        lab.place(x=25,y=30)

        lab=Label(roo1,text="1.  Add new Password",fg="steel blue",font=('arial',12,'bold'))
        lab.place(x=50,y=85)
        lab=Label(roo1,text="2.  Update password",fg="steel blue",font=('arial',12,'bold'))
        lab.place(x=50,y=110)
        lab=Label(roo1,text="3.  Delete password",fg="steel blue",font=('arial',12,'bold'))
        lab.place(x=50,y=135)



        btnshowdb=Button(roo1,text="Add",width=10,fg="steel blue",font=('arial',10),command=addpass)
        btnshowdb.place(x=250,y=85)

        btnseldb=Button(roo1,text="Update",width=10,fg="steel blue",font=('arial',10),command=updatepass)
        btnseldb.place(x=250,y=110)

        btncrtable=Button(roo1,text="Delete",width=10,fg="steel blue",font=('arial',10),command=deletepass)
        btncrtable.place(x=250,y=135)

        roo.mainloop()

    except:
        #reset()
        err=Label(f1,text="Error!!",font=('arial',15,'bold'),fg="red")
        err.place(x=265,y=250)

root=Tk()
root.geometry("700x320+0+0")
root.title("SIMPLIFYING MYSQL")
f1=Frame(root,width=700,height=320,relief=SUNKEN)
f1.pack(side=LEFT)

username_input=StringVar()
passname_input=StringVar()

heading=Label(f1,text="Please enter your credentials",fg="steel blue",font=('arial',20,'bold'))
heading.place(x=150,y=20)
heading=Label(f1,text="********************************************",fg="steel blue",font=('arial',20,'bold'))
heading.place(x=100,y=60)

hostname=Label(f1,text="Hostname : ",font=('arial',15,'bold'))
hostname.place(y=100,x=200)
host=ttk.Combobox(f1,values=["localhost"],)
host.place(x=318,y=107)
host.current(0)

mysqlusername=Label(f1,text="Username : ",font=('arial',15,'bold'))
mysqlusername.place(y=130,x=200)
mysqluser=Entry(f1,font=('arial',10,'bold'),textvariable=username_input)
mysqluser.place(x=319,y=135)

mysqlpassword=Label(f1,text="Password : ",font=('arial',15,'bold'))
mysqlpassword.place(y=160,x=200)
mysqlpass=Entry(f1,font=('arial',10,'bold'),textvariable=passname_input,show="*")
mysqlpass.place(x=318,y=165)

btnlogin=Button(f1,padx=8,pady=1, bd=6 ,fg="black",font=('ariel' ,12,'bold'), text="Submit",command=login)
btnlogin.place(x=230,y=200)

btnreset=Button(f1,padx=8,pady=1, bd=6 ,fg="black",font=('ariel' ,12,'bold'), text="Reset",command=reset)
btnreset.place(x=355,y=200)

root.mainloop()