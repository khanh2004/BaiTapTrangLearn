from tkinter import ttk 
from tkinter import *

shop_management = Tk()


danh_sach_mon_an = [["mì tôm","25000"], ["phở","35000"]]
counting_variable = -1



def open ():
    shop_management.deiconify()
    giao_dien_chinh_sua = Toplevel()
    giao_dien_chinh_sua.mainloop()
    global danh_sach_mon_an
    global counting_variable
    my_tree = ttk.Treeview(giao_dien_chinh_sua)
    my_tree["column"] = ("ten_mon_an", "don_gia")
    my_tree.column("ten_mon_an", anchor=W)
    my_tree.column("don_gia", anchor=W)

    my_tree.heading("ten_mon_an",text=" tên món ăn", anchor=N)
    my_tree.heading("don_gia",text="đơn giá VNĐ", anchor=N )

    for item in range(len(danh_sach_mon_an)) :
        counting_variable = counting_variable + 1
        my_tree.insert(parent="", index=END, values=(danh_sach_mon_an[counting_variable]))
        my_tree.pack()


def open1():
    
    giao_dien_hoa_don = Toplevel()
    hoa_don_label = Label(giao_dien_hoa_don, text="in ra hóa đơn")
    hoa_don_label.pack()
    




ten_app_label = Label(shop_management, text="APP QUAN LI NHA HANG").grid(row=0, column=0, columnspan=2)
danh_sach_mon_button = Button(shop_management, text="chinh sua danh sach mon", padx=40, pady=50, borderwidth=5, command=open).grid(row=1, column=0)
tao_hoa_don_ = Button(shop_management, text="tao hoa don", padx=50, pady=50, borderwidth=5,command=open1).grid(row=1, column=1)





mainloop()