from tkinter import Tk, Entry, Button, StringVar

class Calculator:

    def __init__(self, master):
        master.title("Calculator 🧮")
        master.geometry('357x420+0+0')
        master.config(bg='lightgreen')
        master.resizable(False, False)
        self.equation = StringVar()
        self.entry_value = ''

        Entry(master, width=17, bg="#90EE90", font=('Arial', 28), textvariable=self.equation, bd=1, relief='ridge').place(x=0, y=0)

        button_width = 11
        button_height = 4
        button_padx = 2
        button_pady = 2
        button_relief = 'ridge'
        button_bd = 2

        Button(master, width=button_width, height=button_height, text="(", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show('(')).place(x=0, y=50)
        Button(master, width=button_width, height=button_height, text=")", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(')')).place(x=90, y=50)
        Button(master, width=button_width, height=button_height, text="%", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show('%')).place(x=180, y=50)
        Button(master, width=button_width, height=button_height, text="1", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(1)).place(x=0, y=125)
        Button(master, width=button_width, height=button_height, text="2", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(2)).place(x=90, y=125)
        Button(master, width=button_width, height=button_height, text="3", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(3)).place(x=180, y=125)
        Button(master, width=button_width, height=button_height, text="4", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(4)).place(x=0, y=200)
        Button(master, width=button_width, height=button_height, text="5", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(5)).place(x=90, y=200)
        Button(master, width=button_width, height=button_height, text="6", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(6)).place(x=180, y=200)
        Button(master, width=button_width, height=button_height, text="7", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(7)).place(x=0, y=275)
        Button(master, width=button_width, height=button_height, text="8", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(8)).place(x=90, y=275)
        Button(master, width=button_width, height=button_height, text="9", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(9)).place(x=180, y=275)
        Button(master, width=button_width, height=button_height, text="0", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(0)).place(x=90, y=350)
        Button(master, width=button_width, height=button_height, text=".", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show(".")).place(x=180, y=350)
        Button(master, width=button_width, height=button_height, text="+", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show('+')).place(x=270, y=275)
        Button(master, width=button_width, height=button_height, text="-", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show('-')).place(x=270, y=200)
        Button(master, width=button_width, height=button_height, text="/", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show('/')).place(x=270, y=50)
        Button(master, width=button_width, height=button_height, text="x", relief=button_relief, bg="white", bd=button_bd, command=lambda: self.show('*')).place(x=270, y=125)
        Button(master, width=button_width, height=button_height, text="=", relief=button_relief, bg="lightgreen", bd=button_bd, command=self.solve).place(x=270, y=350)
        Button(master, width=button_width, height=button_height, text="C", relief=button_relief, bg="white", bd=button_bd, command=self.clear).place(x=0, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except:
            self.equation.set("Error")
            self.entry_value = ""

root = Tk()
calculator = Calculator(root)
root.mainloop()
