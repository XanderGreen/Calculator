# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import math

class Calc(): #making it simpler :)
    def __init__(self): #how the numbers are entered - starts off with 0
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False
        #self.myAttr = __float__
        
    def num_press(self, num): #coding for button presses
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self): #calculate total
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value): #what is displayed in the text box
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self): #specific functions
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)
        
    def do_pow(self):
        self.current = float(self.current)
        self.current = math.pow(self.current,2.0)
        self.total = self.current
        self.display(self.total)
        
    def do_sqrt(self):
        self.current = float(self.current)
        self.current = math.sqrt(self.current)
        self.total = self.current
        self.display(self.total)
        
    def do_pi(self):
        self.current = math.pi
        self.current = float(self.current)
        self.total = self.current
        self.display(self.total)

    def operation(self, op): #different operations
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self): #deletes what was just done
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self): #deletes everything
        self.cancel()
        self.total = 0

    def sign(self): #changes sign
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)
        
x = int
        
sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Scientific Calculator")
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row = 0, column = 0, columnspan = 4, sticky=EW)
text_box.insert(0, "0")
text_box.config(bg="black", foreground="white")

numbers = "789456123"
i = 0
bttn = []
for j in range(1,4): #builds buttons automatically :D
    for k in range(3):
        bttn.append(Button(calc, text = numbers[i]))
        bttn[i].grid(row = j, column = k, sticky=EW)
        bttn[i].config(bg="sky blue")
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1
        
bttn_0 = Button(calc, text = "0")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 0, sticky=EW, columnspan=2)
bttn_0.config(bg="sky blue")

bttn_div = Button(calc, text = chr(247))
bttn_div["command"] = lambda: sum1.operation("divide")
bttn_div.grid(row = 1, column = 3, sticky=EW)
bttn_div.config(bg="dodger blue")

bttn_mult = Button(calc, text = "x")
bttn_mult["command"] = lambda: sum1.operation("times")
bttn_mult.grid(row = 2, column = 3, sticky=EW)
bttn_mult.config(bg="dodger blue")

minus = Button(calc, text = "-")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, sticky=EW)
minus.config(bg="dodger blue")

point = Button(calc, text = ".")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 2, sticky=EW)
point.config(bg="sky blue")

add = Button(calc, text = "+")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3, sticky=EW)
add.config(bg="dodger blue")

neg= Button(calc, text = "+/-")
neg["command"] = sum1.sign
neg.grid(row = 5, column = 0, sticky=EW)
neg.config(bg="dodger blue")

clear = Button(calc, text = "C")
clear["command"] = sum1.cancel
clear.grid(row = 5, column = 1, sticky=EW)
clear.config(bg="dodger blue")

all_clear = Button(calc, text = "AC")
all_clear["command"] = sum1.all_cancel
all_clear.grid(row = 5, column = 2, sticky=EW)
all_clear.config(bg="dodger blue")

equals = Button(calc, text = "=")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 3, sticky=EW)
equals.config(bg="dodger blue")

pi = Button(calc, text = "π")
pi["command"] = sum1.do_pi
pi.grid(row = 1, column = 4, sticky=EW)
pi.config(bg="deep sky blue")

sqrt = Button(calc, text = "√")
sqrt["command"] = sum1.do_sqrt
sqrt.grid(row = 4, column = 4, sticky=EW)
sqrt.config(bg="deep sky blue")

squared = Button(calc, text = "x²")
squared["command"] = sum1.do_pow
squared.grid(row = 2, column = 4, sticky=EW)
squared.config(bg="deep sky blue")

root.mainloop()