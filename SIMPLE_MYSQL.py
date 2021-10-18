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
    
    #***************************************SELECT DATABASE**********************
    def seldb():
        
        viewframe=Tk()
        viewframe.geometry("350x280+0+0")
        dbname=StringVar(viewframe)
        dbname.set("")
        lab=Label(viewframe,text="Select from following dbs",fg="green",font=('arial',15,'bold'))
        lab.place(x=50,y=25)
        lab=Label(viewframe,text="**************************************",fg="green",font=('arial',15,'bold'))
        lab.place(x=20,y=50)

        sql="SHOW DATABASES;"
        cursor.execute(sql)
        dbs=cursor.fetchall()
        _connection.commit()
        k=0
        list=[]
        dbses=Frame(viewframe,width=350,height=150,relief=FLAT)
        dbses.place(x=0,y=70)

        scrollbar = Scrollbar(viewframe)
        scrollbar.pack(side=RIGHT, fill=Y)
        listb=Listbox(viewframe,width=31,height=6,relief=FLAT,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        listb.place(x=30,y=80)
                #tkinter.ttk.Separator(roo, orient=VERTICAL).grid(column=1, row=0, colspan=2, sticky='ns')
        for db in dbs:
            s=str(db)
            le=len(s)
            list.append(s)
            k=k+1
            listb.insert(END,str(str(k)+".  "+s[2:le-3:1]))

        lab=Label(viewframe,text="DB_Name:",fg="green",font=('arial',12,'bold'))
        lab.place(x=10,y=220)
        ent=Entry(viewframe,font=('arial',10,'bold'),textvariable=dbname)
        ent.place(x=107,y=222)
        name=dbname.get()
        dbname.set(name)

        def popup():
            newf=Tk()
            newf.geometry("200x100+0+0")
            def destroy():
                newf.destroy()
                viewframe.destroy()
            Button(newf,padx=4,pady=0,bd=4,fg="black",font=('ariel',10,'bold'),text="Done!",command=destroy).place(x=70,y=40)
        def selectdata():
            s=str(dbname.get())
            try:
                sql="USE %s" % (s,)
                cursor.execute(sql)
                _connection.commit()
                a_database_is_selected="YES"
            except:
                Label(viewframe,text="Error!!",fg="red",font=('arial',12,'bold')).place(x=150,y=250)
            if(a_database_is_selected=="YES"):
                popup()
                
        btnsel=Button(viewframe,padx=4,pady=0, bd=4 ,fg="black",font=('ariel' ,10,'bold'), text="Select",command=selectdata)
        
        btnsel.place(x=260,y=220)

    #***************************************CREATE TABLE************************
    def createtable():
        viewframe=Tk()
        viewframe.geometry("400x100+0+0")
        tblname=StringVar(viewframe)
        tblname.set("")
        lab=Label(viewframe,text="Table_Name:",fg="green",font=('arial',12,'bold'))
        lab.place(x=20,y=30)
        ent=Entry(viewframe,font=('arial',10,'bold'),textvariable=tblname)
        ent.place(x=135,y=32)
        name=tblname.get()
        tblname.set(name)
        def create():
            try:
                s=str(tblname.get())
                sql="CREATE TABLE %s (ID INT NOT NULL AUTO_INCREMENT,NAME VARCHAR(20),EMAIL VARCHAR(20),PRIMARY KEY(ID))" % s
                cursor.execute(sql)
                _connection.commit()
            except:
                Label(viewframe,text="Error!!",fg="red",font=('arial',12,'bold')).place(x=155,y=60)

        Button(viewframe,padx=4,pady=0, bd=4 ,fg="black",font=('ariel' ,10,'bold'), text="create",command=create).place(x=300,y=28)
    #***************************************INSERT INTO TABLE*******************
    def insertintotable():
        viewframe=Tk()
        viewframe.geometry("350x200+0+0")
        tblname=StringVar(viewframe)
        tblname.set("")
        custname=StringVar(viewframe)
        custname.set("")
        custemail=StringVar(viewframe)
        custemail.set("")
        Label(viewframe,text="Table_Name:",fg="green",font=('arial',12,'bold')).place(x=40,y=30)
        Entry(viewframe,font=('arial',10,'bold'),textvariable=tblname).place(x=160,y=30)
        name=tblname.get()
        tblname.set(name)
        Label(viewframe,text="Name:",fg="green",font=('arial',12,'bold')).place(x=40,y=70)
        Entry(viewframe,font=('arial',10,'bold'),textvariable=custname).place(x=160,y=70)
        name=custname.get()
        custname.set(name)
        Label(viewframe,text="E-MAIL:",fg="green",font=('arial',12,'bold')).place(x=40,y=110)
        Entry(viewframe,font=('arial',10,'bold'),textvariable=custemail).place(x=160,y=110)
        name=custemail.get()
        custemail.set(name)
        def insert():
            s1=str(tblname.get())
            s2=str(custname.get())
            s3=str(custemail.get())
            try:
                sql="INSERT INTO %s (NAME,EMAIL) VALUES ('%s','%s')" % (s1,s2,s3)
                cursor.execute(sql)
                _connection.commit()
            except:
                Label(viewframe,text="Error!!",fg="red",font=('arial',12,'bold')).place(x=10,y=200)
        Button(viewframe,padx=4,pady=0, bd=4 ,fg="black",font=('ariel' ,10,'bold'), text="INSERT",command=insert).place(x=140,y=140)
    #***************************************SELECT FROM TABLE*******************
    def selectfromtable():
        viewframe=Tk()
        viewframe.geometry("350x300+0+0")
        hr=Frame(viewframe,width=300,height=100,relief=SUNKEN)
        content=Frame(viewframe,width=300,height=200,relief=SUNKEN)
        hr.grid()
        content.grid()
        tblname=StringVar(hr)
        tblname.set("")
        lab=Label(hr,text="Table_Name:",fg="green",font=('arial',12,'bold'))
        lab.place(x=10,y=50)
        ent=Entry(hr,font=('arial',10,'bold'),textvariable=tblname)
        ent.place(x=110,y=50)
        name=tblname.get()
        tblname.set(name)
        def select():
            try:
                s=str(tblname.get())
                sql="SELECT * FROM  %s" % s
                #cursor=_connection.cursor(buffered=True)
                cursor.execute(sql)
                _connection.commit()
                record=cursor.fetchall()
                i=0
                data=[[] for i in range(0,cursor.rowcount)]
                for row in record:
                    for j in range(0,len(row)):
                        data[i].append(str(row[j]))
                    i=i+1
                Label(content,text="ID",fg="steel blue",font=('arial',12,'bold')).place(x=20,y=0)
                Label(content,text="NAME",fg="steel blue",font=('arial',12,'bold')).place(x=100,y=0)
                Label(content,text="EMAIL",fg="steel blue",font=('arial',12,'bold')).place(x=180,y=0)

                for i in range(0,cursor.rowcount):
                    for j in range(0,len(data[0])):
                        Label(content,text=data[i][j],fg="green",font=('arial',10)).place(x=20+80*j,y=30+30*i)
            except:
                def popup():
                    newf=Tk()
                    newf.geometry("200x100+0+0")
                    def dest():
                        newf.destroy()
                        viewframe.destroy()
                    Button(newf,padx=4,pady=0,fg="black",font=('arial',10,'bold'),text="Error!!",command=dest).place(x=70,y=40)
                popup()
                #Label(viewframe,text="Error!!",fg="red",font=('arial',12,'bold')).place(x=150,y=80)
        Button(viewframe,padx=4,pady=0, bd=4 ,fg="black",font=('ariel' ,10,'bold'), text="Select",command=select).place(x=260,y=45)

    def showdatabases():
        dbname=StringVar()
        dbname.set("")
        viewframe=Tk()
        viewframe.geometry("350x300+0+0")

        lab=Label(viewframe,text="Available Databases",fg="green",font=('arial',15,'bold'))
        lab.place(x=50,y=25)
        lab=Label(viewframe,text="********************************",fg="green",font=('arial',15,'bold'))
        lab.place(x=20,y=50)

        sql="SHOW DATABASES;"
        cursor.execute(sql)
        dbs=cursor.fetchall()
        _connection.commit()
        k=0
        list=[]
        dbses=Frame(viewframe,width=350,height=150,relief=FLAT)
        dbses.place(x=0,y=70)

        scrollbar = Scrollbar(viewframe)
        scrollbar.pack(side=RIGHT, fill=Y)
        listb=Listbox(viewframe,width=31,height=8,relief=FLAT,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        listb.place(x=30,y=80)
                #tkinter.ttk.Separator(roo, orient=VERTICAL).grid(column=1, row=0, colspan=2, sticky='ns')
        for db in dbs:
            s=str(db)
            le=len(s)
            list.append(s)
            k=k+1
            listb.insert(END,str(str(k)+".  "+s[2:le-3:1]))
    #**************************************WORKING*****************************

    host="localhost"
    name=str(username_input.get())
    passwd=str(passname_input.get())
    try:
        global _connection
        _connection = None
        if not _connection:
            _connection= mysql.connector.connect(
            host="localhost",
            user=name,
            passwd=passwd,
            buffered=True
            #user=name,
            #passwd=passwd
        )
        global cursor

        cursor=_connection.cursor()

        #*******************************NEW WINDOW****************************
        roo=Tk()
        roo.geometry("400x250+0+0")
        
        
        lab=Label(roo,text="Available Options:",fg="green",font=('arial',15,'bold'))
        lab.place(x=25,y=30)

        lab=Label(roo,text="1.  Create Database",fg="steel blue",font=('arial',12,'bold'))
        lab.place(x=50,y=85)
        lab=Label(roo,text="2.  Select Database",fg="steel blue",font=('arial',12,'bold'))
        lab.place(x=50,y=110)
        lab=Label(roo,text="3.  Create Table",fg="steel blue",font=('arial',12,'bold'))
        lab.place(x=50,y=135)
        lab=Label(roo,text="4.  Insert Into Table",fg="steel blue",font=('arial',12,'bold'))
        lab.place(x=50,y=160)
        lab=Label(roo,text="5.  Select From Table",fg="steel blue",font=('arial',12,'bold'))
        lab.place(x=50,y=185)


        btnshowdb=Button(roo,text="Databases",width=10,fg="steel blue",font=('arial',10),command=showdatabases)
        btnshowdb.place(x=250,y=85)

        btnseldb=Button(roo,text="Select DB",width=10,fg="steel blue",font=('arial',10),command=seldb)
        btnseldb.place(x=250,y=110)

        btncrtable=Button(roo,text="Create Table",width=10,fg="steel blue",font=('arial',10),command=createtable)
        btncrtable.place(x=250,y=135)

        btninsdata=Button(roo,text="Insert Data",width=10,fg="steel blue",font=('arial',10),command=insertintotable)
        btninsdata.place(x=250,y=160)

        btnseldata=Button(roo,text="Select Data",width=10,fg="steel blue",font=('arial',10),command=selectfromtable)
        btnseldata.place(x=250,y=185)
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