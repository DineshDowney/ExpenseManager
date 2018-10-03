from tkinter import *
import exp_back as bk
window=Tk()
window.wm_title("Expenditureee")
def search_ent():
	listb1.delete(0,END)
	for x in bk.search(name.get(),amount.get(),date.get(),nature.get()):
		listb1.insert(END,x)
	
def view_bal():
	listb1.delete(0,END)
	listb1.insert(END,bk.cal_bal())
	
def view_log():
	listb1.delete(0,END)
	for x in bk.view_ent():
		listb1.insert(END,x)

def add_ent():
	bk.insert_ent(name.get(),amount.get(),date.get(),nature.get())
	listb1.delete(0,END)
	listb1.insert(END,(name.get(),amount.get(),date.get(),nature.get()))

def delete_ent():
	bk.delete(name.get(),amount.get(),date.get())
	
lb1=Label(window,text="Name")
lb1.grid(row=1,column=0)

name=StringVar()
e1=Entry(window,textvariable=name)
e1.grid(row=1,column=1)

lb2=Label(window,text="Amount")
lb2.grid(row=1,column=2)

amount=StringVar()
e2=Entry(window,textvariable=amount)
e2.grid(row=1,column=3)

lb3=Label(window,text="Date")
lb3.grid(row=2,column=0)

date=StringVar()
e3=Entry(window,textvariable=date)
e3.grid(row=2,column=1)

lb4=Label(window,text="Nature")
lb4.grid(row=2,column=2)

nature=StringVar()
e4=Entry(window,textvariable=nature)
e4.grid(row=2,column=3)

listb1=Listbox(window,height=8,width=38)
listb1.grid(row=3,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=3,column=2,rowspan=6)

listb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=listb1.yview)

def get_id(event):
	global row
	index=listb1.curselection()[0]
	row=listb1.get(index)
	e1.delete(0,END)
	e1.insert(END,row[0])
	e2.delete(0,END)
	e2.insert(END,row[1])
	e3.delete(0,END)
	e3.insert(END,row[2])
	e4.delete(0,END)
	e4.insert(END,row[3])	
listb1.bind('<<ListboxSelect>>',get_id)

bt1=Button(window,text="Add Entry",command=add_ent,width=13)
bt1.grid(row=3,column=3)

bt2=Button(window,text="View Balance",command=view_bal,width=13)
bt2.grid(row=4,column=3)

bt3=Button(window,text="View Logs",command=view_log,width=13)
bt3.grid(row=5,column=3)

bt4=Button(window,text="Search Entry",command=search_ent,width=13)
bt4.grid(row=6,column=3)

bt5=Button(window,text="Delete Entry",command=delete_ent,width=13)
bt5.grid(row=7,column=3)

bt6=Button(window,text="Close",command=window.destroy,width=13)
bt6.grid(row=8,column=3)

window.mainloop()