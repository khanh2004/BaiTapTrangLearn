from tkinter import *
from tkinter import BOTH, END, LEFT

my_w = Tk()
menu={0:['mì tôm',20000],1:['phở',35000],2:['cơm rang',25000],
3:['bún',20000],4:['bánh mì',15000],5:['pepsi',8000],
6:['aquafina',5000],7:['coca',10000]}
sb=[]
sv1=IntVar()
sb1 = Spinbox(my_w ,from_=0,to_=5,width=1,textvariable=sv1)
sb1.grid(row=1,column=0,padx=100,pady=100)
sb.append(sb1)  
print(sb)
mainloop()