from re import L
from tkinter import ttk 
from tkinter import *
from tkinter import messagebox

ten_mon_can_xoa = ""
danh_sach_mon_an = [["mì tôm","25000"], ["phở","35000"]]
shop_management = Tk()
def open1():    
    giao_dien_hoa_don = Toplevel()
    hoa_don_label = Label(giao_dien_hoa_don, text="in ra hóa đơn")
    hoa_don_label.pack()

def xoa_mon():
    giao_dien_xoa_mon = Toplevel()
    ten_mon_can_xoa_label = Label(giao_dien_xoa_mon, text="tên món cần xóa")
    ten_mon_can_xoa_entry = Entry(giao_dien_xoa_mon,width=30)
    thong_bao_da_xoa_mon_an_button = Button(giao_dien_xoa_mon, text="xoa!",command=an_nut_xoa)

    ten_mon_can_xoa_label.grid(column=0, row=0)
    ten_mon_can_xoa_entry.grid(column=1, row=0)
    thong_bao_da_xoa_mon_an_button.grid(column=1,row=2)
    ten_mon_can_xoa = ten_mon_can_xoa_entry.get()
     
def an_nut_xoa ():
        global ten_mon_can_xoa   
        for ten_mon_an in danh_sach_mon_an:
            if ten_mon_can_xoa in ten_mon_an :
                messagebox.showwarning("thông báo xóa món","đã xóa món thành công")
            else:
                messagebox.showwarning("thông báo xóa món","xóa món không thành công")
           
def open ():
    counting_variable = -1
    giao_dien_chinh_sua = Toplevel()
    global danh_sach_mon_an
    my_tree = ttk.Treeview(giao_dien_chinh_sua)
    my_tree["column"] = ("ten_mon_an", "don_gia")
    my_tree.column("ten_mon_an")
    my_tree.column("don_gia")
    
    my_tree.heading("ten_mon_an",text=" tên món ăn", anchor=N)
    my_tree.heading("don_gia",text="đơn giá VNĐ", anchor=N )
    
    for ten_mon_an in range(len(danh_sach_mon_an)) :
        counting_variable = counting_variable + 1
        my_tree.insert(parent="", index=END, values=(danh_sach_mon_an[counting_variable]))
        my_tree.pack()
    xoa_mon_button = Button(giao_dien_chinh_sua,text="xoá món ăn",command=xoa_mon).pack() 
print(ten_mon_can_xoa)   
     
ten_app_label = Label(shop_management, text="APP QUAN LI NHA HANG").grid(row=0, column=0, columnspan=2)
danh_sach_mon_button = Button(shop_management, text="chinh sua danh sach mon", padx=40, pady=50, borderwidth=5, command=open).grid(row=1, column=0)
tao_hoa_don_ = Button(shop_management, text="tao hoa don", padx=50, pady=50, borderwidth=5,command=open1).grid(row=1, column=1)

mainloop()