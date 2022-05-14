history_file = open("C:/Users/Administrator/Desktop/hoang_duy_khanh/his.csv", mode="w", encoding="utf-8-sig")

from tkinter import *
from tkinter import ttk
import time

menu={0:['bánh mì', 15000], 1:['mì tôm', 20000], 2:['phở', 35000], 
3:['bún', 20000], 4:['quafina', 6000], 5:['pepsi', 9000], 
6:['coca', 10000], 7:['7 up', 8000]}
oders = []
history  = []


app_tinh_tien =Tk()
app_tinh_tien.geometry("900x400") 

second_frame = Frame(app_tinh_tien)
firts_frame = Frame(app_tinh_tien, bg='#bfedf2')

firts_frame.grid(row=1, column=0)
second_frame.grid(row=1, column=1)

oders_treeview = ttk.Treeview(second_frame)
oders_treeview.grid(row=0, column=0, columnspan=2, padx=3, pady=2)

oders_treeview["columns"] = ("1",  "2", "3")
oders_treeview.column("#0",  width=80)
oders_treeview.column("1",  width=80)
oders_treeview.column("2",  width=80 )
oders_treeview.column("3",  width=80)
oders_treeview.heading("#0",  text="đơn hàng")
oders_treeview.heading("1",  text="đơn giá")
oders_treeview.heading("2",  text="số lượng")
oders_treeview.heading("3",  text="tổng cộng")
def lam_moi():
    global current_time
    for item in oders_treeview.get_children():
        history.append(item)
        oders_treeview.delete(item)
    

    my_list=[]
    for i in range(8):
        my_list.append(IntVar(value=0))
    for i in range(len(oders)):
        print(oders[i].config(textvariable=my_list[i]))

    for w in second_frame.grid_slaves(2):
        w.grid_remove()    
    for w in second_frame.grid_slaves(3):
        w.grid_remove()
    for w in second_frame.grid_slaves(4):
        w.clipboard_append(history)
        w.grid_remove()
    new_bill = str(history)
    history_file.write(new_bill + "\n")
    
def thanh_toan():
    total = 0
    for item in oders_treeview.get_children():
        oders_treeview.delete(item)
    for i in range(len(oders)):
        if(int(oders[i].get())>0):
            price=int(oders[i].get())*menu[i][1]
            total=total+price
            my_str1=(str(menu[i][1]),  str(oders[i].get()),  str(price))
            oders_treeview.insert("", 'end', iid=i, text=menu[i][0], values=my_str1)
    current_time = time.asctime()
    tong_tien_label = Label(second_frame,  text="tổng cộng",  font=32)
    tong_tien_label.grid(row=3, column=0)
    tong_tien_value = Label(second_frame, text=str(total)+"VNĐ", font=32)
    tong_tien_value.grid(row=3, column=1)
    thoi_gian_label = Label(second_frame, text=current_time)
    thoi_gian_label.grid(row=4, column=1)

    
pdx, pdy=40,5

menu1 = Label(firts_frame, text="bánh mì")
menu1.grid(row=0, column=0, padx=pdx, pady=pdy)    
menu2 = Label(firts_frame, text="mì tôm")
menu2.grid(row=0, column=1, padx=pdx, pady=pdy)
menu3 = Label(firts_frame, text="phở")
menu3.grid(row=0, column=2, padx=pdx, pady=pdy)
menu4 = Label(firts_frame, text="bún")
menu4.grid(row=0, column=3, padx=pdx, pady=0)
r_1 = IntVar()
oders1 = Spinbox(firts_frame, from_=0, to_=5, font=20, width=1, textvariable=r_1)
oders1.grid(row=1, column=0, padx=pdx, pady=0)
oders.append(oders1)    
r_2 = IntVar()
oders2 = Spinbox(firts_frame, from_=0, to_=5, font=20, width=1, textvariable=r_2)
oders2.grid(row=1, column=1, padx=pdx, pady=0)
oders.append(oders2)    
r_3 = IntVar()
oders3 = Spinbox(firts_frame,  from_=0, to_=5,  font=20,  width=1,  textvariable=r_3)
oders3.grid(row=1, column=2, padx=pdx, pady=0)
oders.append(oders3)    
r_4 = IntVar()
oders4 = Spinbox(firts_frame,  from_=0, to_=5,  font=20,  width=1,  textvariable=r_4)
oders4.grid(row=1, column=3, padx=pdx, pady=0)
oders.append(oders4)    
menu5 = Label(firts_frame, text="aquafina")
menu5.grid(row=2,  column=0,  padx=pdx,  pady=pdy)
menu6 = Label(firts_frame, text="pepsi")
menu6.grid(row=2,  column=1,  padx=pdx,  pady=pdy)
menu7 = Label(firts_frame,  text="coca")
menu7.grid(row=2, column=2, padx=pdx, pady=pdy)
menu8 = Label(firts_frame, text="7 up")
menu8.grid(row=2, column=3, padx=pdx, pady=pdy)
r_5 = IntVar()
oders5 = Spinbox(firts_frame, from_=0, to_=5, font=20, width=1, textvariable=r_5)
oders5.grid(row=3, column=0, padx=pdx, pady=pdy)
oders.append(oders5)
r_6 = IntVar()
oders6 = Spinbox(firts_frame, from_=0, to_=5, font=20, width=1, textvariable=r_6)
oders6.grid(row=3, column=1, padx=pdx, pady=pdy)
oders.append(oders6)
r_7 = IntVar()
oders7 = Spinbox(firts_frame, from_=0, to_=5, font=20, width=1, textvariable=r_7)
oders7.grid(row=3, column=2, padx=pdx, pady=pdy)
oders.append(oders7)
r_8=IntVar()
oders8 = Spinbox(firts_frame, from_=0, to_=5, font=20, width=1, textvariable=r_8)
oders8.grid(row=3, column=3, padx=pdx, pady=pdy)
oders.append(oders8)
thanh_toan_button = Button(firts_frame, text="Get Bill", command=thanh_toan)
thanh_toan_button.grid(row=4,  column=1, )
lam_moi_button = Button(firts_frame, text="làm mới", command=lam_moi)
lam_moi_button.grid(row=4,  column=2)
app_tinh_tien.mainloop()
