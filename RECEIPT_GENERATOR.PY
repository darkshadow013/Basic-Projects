from tkinter import *
import mysql.connector
from tkinter.filedialog import *
import random
import os
from tkinter import messagebox
from datetime import date
from pathlib import Path
from stat import S_IREAD, S_IRGRP, S_IROTH
def calculate():
	if(str(invoice_no.get())[0:4:1]!="Bill"):
		sql="SELECT * FROM BILLS"
		cursor.execute(sql)
		_connection.commit()
		invoice_no.set("Bill"+ str(cursor.rowcount+1))
	n=float(quantity.get())
	m=float(mrp.get())
	p=n*m
	disc=float(discount.get())
	pri=((100-disc)*p)/100
	vt=float(vat.get())
	tax=pri*(vt/100)
	pri=pri+tax
	total_price.set(str(pri))
	total_tax.set(str(tax))
def save():
	filename =asksaveasfilename(filetypes = (("txt files","*.txt"),("all files","*.*")),defaultextension=".txt")
	f = open(filename,'w')
	f.write(billarea.get('1.0', 'end'))
	f.close()
	messagebox.showinfo("FYI", "File Saved %s" % str(os.getcwd()) )
	s1=str(firm_name.get())
	s2=str(date.today().strftime("%d/%m/%Y"))
	s3=str(pin_code.get())
	s4=str(invoice_no.get())
	s5=str(total_price.get())
	sql="INSERT INTO BILLS (FIRM_NAME,DATE,PIN_CODE,INVOICE_NO,AMOUNT) VALUES ('%s','%s','%s','%s','%s')" % (s1,s2,s3,s4,s5)
	cursor.execute(sql)
	_connection.commit()
	reset()
	billarea.config(state=NORMAL)
	billarea.delete("1.0",END)
def printv():
	calculate()
	billarea.delete("1.0",END)
	billarea.insert(END,'\n     '+str(firm_name.get()).upper()+"\t\t\t\t    Invoice :"+invoice_no.get()+'\n')
	billarea.insert(END,'     '+str(shop_no.get())+','+str(street_name.get().upper())+"\t\t\t\t    Date    :"+date.today().strftime("%d/%m/%Y")+'\n')
	billarea.insert(END,'     '+str(city_name.get().upper())+','+str(pin_code.get())+'\n')
	billarea.insert(END,'\n\n\t\t Brand Name    : '+brand_name.get().upper()+'\n')
	billarea.insert(END,'\t\t Article no.   : '+article_no.get().upper()+'\n')
	billarea.insert(END,'\t\t Quantity      : '+quantity.get()+'\n')
	billarea.insert(END,'\t\t M.R.P.        : '+mrp.get()+'\n')
	billarea.insert(END,'\t\t Discount      : '+discount.get()+'\n')
	billarea.insert(END,'\t\t Tax(%)        : '+vat.get()+'\n')
	billarea.insert(END,"        ======================================\n")
	billarea.insert(END,'\t\t Total Tax     : '+total_tax.get()+'\n')
	billarea.insert(END,"        ======================================\n")
	billarea.insert(END,'\t\tTotal Amount   : '+total_price.get()+'\n')
	billarea.config(state=DISABLED)
def reset():
	billarea.delete("1.0",END)
	firm_name.set("")
	invoice_no.set("")
	article_no.set("")
	quantity.set("")
	brand_name.set("")
	mrp.set("")
	discount.set("")
	vat.set("")
	total_tax.set("")
	total_price.set("")
	shop_no.set("")
	street_name.set("")
	city_name.set("")
	pin_code.set("")
global _connection
_connection = None
if not _connection:
    _connection= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="9782132659a@A",
    buffered=True
)

print("conn:- ",_connection)
global cursor
cursor=_connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS BILLS;")

cursor.execute("USE BILLS;")
cursor.execute("CREATE TABLE IF NOT EXISTS BILLS (FIRM_NAME VARCHAR(20),DATE VARCHAR(20),PIN_CODE VARCHAR(20),INVOICE_NO VARCHAR(20),AMOUNT VARCHAR(20));");
_connection.commit()
root=Tk()
root.geometry("1000x620+0+0")
root.config(bg="white")
work=Frame(root,width=300,height=620)
work.pack(side=LEFT)
work.config(bg="white")
output=Frame(root,width=700,height=620,bg="white")
output.pack(side=RIGHT)
firm_name=StringVar(work)
invoice_no=StringVar(work)
article_no=StringVar(work)
quantity=StringVar(work)
brand_name=StringVar(work)
mrp=StringVar(work)
discount=StringVar(work)
vat=StringVar(work)
total_tax=StringVar(work)
total_price=StringVar(work)
shop_no=StringVar(work)
street_name=StringVar(work)
city_name=StringVar(work)
pin_code=StringVar(work)
Label(work,text="Enter Details",bg="white",fg="Steel blue",font=('consolas',18,'bold')).place(x=52,y=20)
Label(work,text="*******************",fg="Steel blue",bg="white",font=('consolas',15,'bold')).place(x=30,y=52)
Label(work,text="Firm name : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=20+60+10)
Label(work,text="Invoice No. : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=50+60+10)
Label(work,text="Shop No. : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=80+60+10)
Label(work,text="Street Name : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=110+60+10)
Label(work,text="City Name : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=140+60+10)
Label(work,text="Pin Code : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=170+60+10)
Label(work,text="Brand Name : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=200+60+10)
Label(work,text="Article no. : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=230+60+10)
Label(work,text="Quantity : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=260+60+10)
Label(work,text="M.R.P. : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=290+60+10)
Label(work,text="Discount : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=320+60+10)
Label(work,text="VAT(%) : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=350+60+10)
Label(work,text="Total Tax : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=380+60+10)
Label(work,text="Total Price : ",fg="black",bg="white",font=('arial',12,'bold')).place(x=10,y=410+60+10)
Entry(work,font=('consolas',10,'bold'),textvariable=firm_name,bg="powder blue").place(x=125,y=95)
Entry(work,font=('consolas',10,'bold'),textvariable=invoice_no,bg="powder blue").place(x=125,y=125)
Entry(work,font=('consolas',10,'bold'),textvariable=shop_no,bg="powder blue").place(x=125,y=155)
Entry(work,font=('consolas',10,'bold'),textvariable=street_name,bg="powder blue").place(x=125,y=185)
Entry(work,font=('consolas',10,'bold'),textvariable=city_name,bg="powder blue").place(x=125,y=215)
Entry(work,font=('consolas',10,'bold'),textvariable=pin_code,bg="powder blue").place(x=125,y=245)
Entry(work,font=('consolas',10,'bold'),textvariable=brand_name,bg="powder blue").place(x=125,y=275)
Entry(work,font=('consolas',10,'bold'),textvariable=article_no,bg="powder blue").place(x=125,y=305)
Entry(work,font=('consolas',10,'bold'),textvariable=quantity,bg="powder blue").place(x=125,y=335)
Entry(work,font=('consolas',10,'bold'),textvariable=mrp,bg="powder blue").place(x=125,y=365)


Entry(work,font=('consolas',10,'bold'),textvariable=discount,bg="powder blue").place(x=125,y=395)
Entry(work,font=('consolas',10,'bold'),textvariable=vat,bg="powder blue").place(x=125,y=425)
Entry(work,font=('consolas',10,'bold'),textvariable=total_tax,bg="powder blue").place(x=125,y=455)
Entry(work,font=('consolas',10,'bold'),textvariable=total_price,bg="powder blue").place(x=125,y=485)
Button(work,font=('arial',10,'bold'),text="Calculate",height=2,width=13,command=calculate).place(x=30,y=515)
Button(work,font=('arial',10,'bold'),text="Print",height=2,width=13,command=printv).place(x=145,y=515)
Button(work,font=('arial',10,'bold'),text="Save",height=2,width=13,command=save).place(x=30,y=555)
Button(work,font=('arial',10,'bold'),text="Reset",height=2,width=13,command=reset).place(x=145,y=555)

output1=Frame(output,width=800,height=100,bg="white")
output1.pack(side=TOP)
output2=Frame(output,width=800,height=400,bg="blue")
output2.pack(side=BOTTOM)
Label(output1,text="Bill Details",font=('consolas',25,'bold'),fg="steel blue",bg="white").grid()
Label(output1,text="***************************",font=('consolas',20,'bold'),fg="steel blue",bg="white").grid()
billarea=Text(output2,width=750,height=400,font=('consolas',15))
scroll=Scrollbar(output2)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=billarea.yview)
billarea.config(yscrollcommand=scroll.set)
billarea.pack()
root.mainloop()
