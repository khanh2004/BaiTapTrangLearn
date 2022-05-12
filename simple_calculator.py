from tkinter import *
simple_calculator = Tk()
simple_calculator.title("Simple Calculator")
lcd_display = Entry(simple_calculator, width=60, borderwidth=5)
lcd_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def add_number(number) :
    displaying = lcd_display.get() 
    lcd_display.delete(0,END)  
    lcd_display.insert(0,str(displaying) + str(number))

def AC_button() :
    lcd_display.delete(0,END)

def plus_button(plus_sign):
    lcd_display.insert(END,plus_sign)

def minus_button() :
    lcd_display.insert(END," - ")

#def multiply_button():
    lcd_display.insert(END," * ")

#def devide_button():
    lcd_display.insert(END," / ")

def equal_button() :
    result = int(lcd_display.get())
    lcd_display.insert(END,result)
#def comma_button():
    lcd_display.insert(END,".")

#def _bracket_button_1():
    lcd_display.insert(END, "(")

#def _bracket_button_2():
    lcd_display.insert(END, ")")

    


butt_1 = Button(simple_calculator, text="1", padx=40, pady=20, command= lambda: add_number(1))
butt_2 = Button(simple_calculator, text="2", padx=40, pady=20, command= lambda: add_number(2))
butt_3 = Button(simple_calculator, text="3", padx=40, pady=20, command= lambda: add_number(3))
butt_4 = Button(simple_calculator, text="4", padx=40, pady=20, command= lambda: add_number(4))
butt_5 = Button(simple_calculator, text="5", padx=40, pady=20, command= lambda: add_number(5))
butt_6 = Button(simple_calculator, text="6", padx=40, pady=20, command= lambda: add_number(6))
butt_7 = Button(simple_calculator, text="7", padx=40, pady=20, command= lambda: add_number(7))
butt_8 = Button(simple_calculator, text="8", padx=40, pady=20, command= lambda: add_number(8))
butt_9 = Button(simple_calculator, text="9", padx=40, pady=20, command= lambda: add_number(9))
butt_0 = Button(simple_calculator, text="0", padx=87.499, pady=20, command= lambda: add_number(0))
equal_butt = Button(simple_calculator, text="=", padx=40, pady=20, command= equal_button)
#comma_butt = Button(simple_calculator, text=".", padx=41, pady=20, command= comma_button)
#bracket_butt_1 = Button(simple_calculator, text="(", padx=41, pady=20, command= _bracket_button_1)
#bracket_butt_2 = Button(simple_calculator, text=")", padx=41, pady=20, command= _bracket_button_2)
AC_butt = Button(simple_calculator, text="AC", padx=35, pady=20, command= AC_button)

plus_butt = Button(simple_calculator, text="+", padx=39, pady=20, command= lambda: plus_button(" + "))
minus_butt = Button(simple_calculator, text="-", padx=40, pady=20, command= minus_button)
#multiply_butt = Button(simple_calculator, text="*", padx=40, pady=20, command= multiply_button)
#devide_butt = Button(simple_calculator, text="/", padx=40, pady=20, command= devide_button)

butt_0.grid(row=5, column=0, columnspan=2 )
butt_1.grid(row=4, column=0 )
butt_2.grid(row=4, column=1 )
butt_3.grid(row=4, column=2 )
butt_4.grid(row=3, column=0 )
butt_5.grid(row=3, column=1 )
butt_6.grid(row=3, column=2 )
butt_7.grid(row=2, column=0 )
butt_8.grid(row=2, column=1 )
butt_9.grid(row=2, column=2 )
AC_butt.grid(row=1, column=0)
plus_butt.grid(row=1, column=3 )
equal_butt.grid(row=5, column=3)
#comma_butt.grid(row=5, column=2)
#bracket_butt_1.grid(row=1, column=1)
#bracket_butt_2.grid(row=1, column=2)
minus_butt.grid(row=2,column=3)
#multiply_butt.grid(row=3,column=3)
#devide_butt.grid(row=4,column=3)

simple_calculator.mainloop()