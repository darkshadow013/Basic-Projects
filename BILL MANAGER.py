import mysql.connector
import getpass

mydb = mysql.connector.connect(
  host="localhost",
  user="DARKSHADOW26",
  passwd="9782132659a@A"
)
def viewbiller():
    name=input("Enter biller you want to find : ")
    sql="CREATE TABLE IF NOT EXISTS %s (AMOUNT VARCHAR(20),DATED VARCHAR(20))" % (name)
    cursor.execute(sql)
    print("AVAILABLE OPTIONS\n1. VIEW RECORD OF SINGLE DATE\n2. VIEW COMPLETE HISTORY OF BILLER %s"%name)
    print("Enter choice: ",end=" ")
    n=int(input())
    count=0
    if(n==1):
        date=input("ENTER DATE OF WHICH YOU WANT TO VIEW BILLS :")
        sql="SELECT AMOUNT FROM %s WHERE DATED=%s" % (name,date)
        cursor.execute(sql)
        for x in cursor:
            count=count+1
            print(count,"-> ",end=" ")
            print(x[0])
            
    if(n==2):
        sql="SELECT * FROM %s" % (name)
        cursor.execute(sql)
        for x in cursor:
            count=count+1
            print(count,"-> ",end=" ")
            print(x[0],end="\t")
            print(x[1])
    if(count==0):
        print("NO ENTRY FOUND!!")

def addbill():
    t=1
    while(t):
        name=input("\nEnter biller name: ")
        date=input("Enter date: ")
        price=input("Enter amount: ")
        sql="INSERT INTO %s (AMOUNT,DATED) VALUES (%s,%s)" % (name,price,date)
        cursor.execute(sql)
        mydb.commit()
        print("\nDO YOU WANT TO CONTINUE?\n\n1. YES\n2. NO  ")
        n=int(input())
        if(n==2):
            t=0
            return

def logout():
    print("LOGOUT SUCESS!!")
    mydb.commit()
    return
def login():
    print("\nEnter gmail email-id:",end=" ")
    name=input()
    password=getpass.getpass()
    str=name[::-1]
    if(str.startswith("moc.liamg@")):
        cursor.execute("SELECT * FROM USERS WHERE EMAIL= %s",(name,))
        data="error"
        for i in cursor:
            data=i
        if data=="error":
            print("\nRECORD NOT FOUND")
            return
        else:
            sql="SELECT * FROM USERS WHERE EMAIL=%s"
            cursor.execute(sql,(name,));
            for x in cursor:
                real=x[1]
            real=password
            if(real == password):
                user=x[0]
                print("\n\t\t\t\tWELCOME %s" % user)
                print("\nAVAILABLE OPTIONS\n1. VIEW BILLER\n2. ADD BILLER\n3. LOGOUT")

                print("\nENTER YOUR CHOICE:",end=" ")
                n=int(input())
                if(n==1):
                    viewbiller()
                if(n==2):
                    addbill()
                if(n==3):
                    logout()

            else:
                print(real)
                print("WRONG PASSWORD")
                return

    else:
        print("Wrong username")
        return

def signup():
    name=input("Enter name of customer : ")
    password=input()
    email=input("Enter email : ")
    #sql="INSERT INTO %s (AMOUNT,DATED) VALUES (%s,%s)" % (name,price,date)
    str="my password is beautiful"
    sql="INSERT INTO USERS (NAME,PASSWORD,EMAIL) VALUES (%s,%s,%s)" 
    val= (name,password,email)
    cursor.execute(sql,val)
    mydb.commit()
    print("\nRegistered Success")

cursor=mydb.cursor();
cursor.execute("CREATE DATABASE IF NOT EXISTS INITIAL")
cursor.execute("USE INITIAL")
sql="CREATE TABLE IF NOT EXISTS USERS (NAME VARCHAR(50),PASSWORD VARCHAR(50),EMAIL VARCHAR(50) PRIMARY KEY)"
cursor.execute(sql)
mydb.commit()
print("\nSELECT YOUR CHOICE\n\n1. LOGIN\n2. SIGN_UP")
print("\nEnter choce: ",end=" ")
n=int(input())
if(n==1):
    login()
else:
    signup()
mydb.close()