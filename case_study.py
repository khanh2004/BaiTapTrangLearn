from tkinter import *
from tkinter import ttk
from tkinter import BOTH, END, LEFT

menu={0:['mì tôm',20000],1:['phở',35000],2:['cơm rang',25000],
3:['bún',20000],4:['bánh mì',15000],5:['pepsi',8000],
6:['aquafina',5000],7:['coca',10000]}
bill=[]

app_tinh_tien = Tk()
app_tinh_tien.geometry("800x300") 

second_frame=Frame(app_tinh_tien)
first_frame=Frame(app_tinh_tien)

first_frame.grid(row=1,column=0)
second_frame.grid(row=1,column=1)

bill_treeview = ttk.Treeview(second_frame)
bill_treeview.grid(row=0,column=0,columnspan=2,padx=3,pady=2)

bill_treeview["columns"] = ("1", "2","3")
bill_treeview.column("#0", width = 80)
bill_treeview.column("1", width = 60)
bill_treeview.column("2", width =50 )
bill_treeview.column("3", width = 50)

bill_treeview.heading("#0", text ="Item")
bill_treeview.heading("1", text ="Price")
bill_treeview.heading("2", text ="qty")
bill_treeview.heading("3", text ="Total")

def thanh_toan():
    total=0
    for item in bill_treeview.get_children():
        bill_treeview.delete(item)
        print(bill)
    for i in range(len(bill)):
        if(int(bill[i].get())>0):
            price=int(bill[i].get())*menu[i][1]
            total=total+price
            mystery_string=(str(menu[i][1]), str(bill[i].get()), str(price))
            bill_treeview.insert("",END,text=menu[i][0],values=mystery_string)
    la_1=Label(second_frame,text='Total')
    la_1.grid(row=1,column=0)
    l_2=Label(second_frame,text=str(total))
    l_2.grid(row=1,column=1)

def clear():
    for item in bill_treeview.get_children():
        bill_treeview.delete(item)
    l1=[]
    for i in range(8):
        l1.append(app_tinh_tien.IntVar(value=0))
    for i in range(len(menu)):
        print(menu[i].config(textvariable=l1[i]))
    for w in second_frame.grid_slaves(1):
        w.grid_remove()
    for w in second_frame.grid_slaves(2):
        w.grid_remove()    
    for w in second_frame.grid_slaves(3):
        w.grid_remove()


pdx,pdy=40,5

menu1=Button(first_frame,text='mì tôm')
menu1.grid(row=0,column=0,padx=pdx,pady=pdy)    
menu2=Button(first_frame,text='phở')
menu2.grid(row=0,column=1,padx=pdx,pady=pdy)
menu3=Button(first_frame,text='cơm rang')
menu3.grid(row=0,column=2,padx=pdx,pady=pdy)
menu4=Button(first_frame,text='bún')
menu4.grid(row=0,column=3,padx=pdx,pady=0)

bill1 = Spinbox(first_frame,from_=0,to_=5,width=1,textvariable=IntVar(), font=(15))
bill1.grid(row=1,column=0,padx=pdx,pady=0)
bill.append(bill1)    

bill2 = Spinbox(first_frame,from_=0,to_=5,width=1,textvariable=IntVar(), font=(15))
bill2.grid(row=1,column=1,padx=pdx,pady=0)
bill.append(bill2)    

bill3 = Spinbox(first_frame,from_=0,to_=5,width=1,textvariable=IntVar(), font=(15))
bill3.grid(row=1,column=2,padx=pdx,pady=0)
bill.append(bill3)    

bill4 = Spinbox(first_frame,from_=0,to_=5,width=1,textvariable=IntVar(), font=(15))
bill4.grid(row=1,column=3,padx=pdx,pady=0)
bill.append(bill4)    
menu5=Button(first_frame,text='bánh mì')
menu5.grid(row=2,column=0,padx=pdx,pady=pdy)
menu6=Button(first_frame,text='pepsi')
menu6.grid(row=2,column=1,padx=pdx,pady=pdy)
menu7=Button(first_frame,text='aquafina')
menu7.grid(row=2,column=2,padx=pdx,pady=pdy)
menu8=Button(first_frame,text='coca')
menu8.grid(row=2,column=3,padx=pdx,pady=pdy)

bill5 = Spinbox(first_frame,from_=0,to_=5,width=1,textvariable=IntVar(), font=(15))
bill5.grid(row=3,column=0,padx=pdx,pady=pdy)
bill.append(bill5)

bill6 = Spinbox(first_frame,from_=0,to_=5,width=1,textvariable=IntVar(), font=(15))
bill6.grid(row=3,column=1,padx=pdx,pady=pdy)
bill.append(bill6)

bill7 = Spinbox(first_frame,from_=0,to_=5,width=1,textvariable=IntVar(), font=(15))
bill7.grid(row=3,column=2,padx=pdx,pady=pdy)
bill.append(bill7)

bill8 = Spinbox(first_frame,from_=0,to_=5,width=1,textvariable=IntVar(), font=(15))
bill8.grid(row=3,column=3,padx=pdx,pady=pdy)
bill.append(bill8)
b1=Button(first_frame,text='thanh toán',command=thanh_toan)
b1.grid(row=4,column=1, pady=20)
b2=Button(first_frame,text='làm mới',command=clear)
b2.grid(row=4,column=2, pady=20)

mainloop()
