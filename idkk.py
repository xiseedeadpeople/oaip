# ceo@

import tkinter as tk
from tkinter import ttk
from math import sqrt


class Calculator:

    # TODO:
    #       - ttk.entry chars deny (19)
    #       - //0 err
    #       - Добавьте информацию о разработчиках на форму программы + Дайте название своему калькулятору
    #       - Поработайте над дизайном своей программы
    #       - Прикрепите к отчету исполняемый файл (.exe)
    # UI
    def __init__(self, master):
        self.master = master
        self.master.title("goofy ahh calc")
        self.master.geometry("300x620")

        self.number_entry = ttk.Entry(self.master, width=20)
        self.number_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.button_1 = ttk.Button(self.master, text="1", command=lambda: self.button_click(1))
        self.button_2 = ttk.Button(self.master, text="2", command=lambda: self.button_click(2))
        self.button_3 = ttk.Button(self.master, text="3", command=lambda: self.button_click(3))
        self.button_4 = ttk.Button(self.master, text="4", command=lambda: self.button_click(4))
        self.button_5 = ttk.Button(self.master, text="5", command=lambda: self.button_click(5))
        self.button_6 = ttk.Button(self.master, text="6", command=lambda: self.button_click(6))
        self.button_7 = ttk.Button(self.master, text="7", command=lambda: self.button_click(7))
        self.button_8 = ttk.Button(self.master, text="8", command=lambda: self.button_click(8))
        self.button_9 = ttk.Button(self.master, text="9", command=lambda: self.button_click(9))
        self.button_0 = ttk.Button(self.master, text="0", command=lambda: self.button_click(0))
        self.button_clear = ttk.Button(self.master, text="C", command=self.button_clear)
        self.button_add = ttk.Button(self.master, text="+", command=self.button_add)
        self.button_equal = ttk.Button(self.master, text="=", command=self.button_equal)
        self.button_subtract = ttk.Button(self.master, text="-", command=self.button_subtract)
        self.button_multiply = ttk.Button(self.master, text="*", command=self.button_multiply)
        self.button_divide = ttk.Button(self.master, text="/", command=self.button_divide)
        self.button_floor_div = ttk.Button(self.master, text="//", command=self.button_floor_div)
        self.button_modulus = ttk.Button(self.master, text="%", command=self.button_modulus)
        self.button_sqrt = ttk.Button(self.master, text="√", command=self.button_sqrt)
        self.button_neg = ttk.Button(self.master, text="+/-", command=self.button_neg)

        # 1st row
        self.button_sqrt.grid(row=0, column=1)
        self.button_modulus.grid(row=0, column=2)
        self.button_floor_div.grid(row=0, column=3)
        self.button_divide.grid(row=0, column=4)

        # 2nd row
        self.button_1.grid(row=1, column=1)
        self.button_2.grid(row=1, column=2)
        self.button_3.grid(row=1, column=3)
        self.button_multiply.grid(row=1, column=4)

        # 3rd row
        self.button_4.grid(row=2, column=1)
        self.button_5.grid(row=2, column=2)
        self.button_6.grid(row=2, column=3)
        self.button_subtract.grid(row=2, column=4)

        # 4rth row
        self.button_7.grid(row=3, column=1)
        self.button_8.grid(row=3, column=2)
        self.button_9.grid(row=3, column=3)
        self.button_add.grid(row=3, column=4)

        # 5th row
        self.button_clear.grid(row=4, column=1)
        self.button_0.grid(row=4, column=2)
        self.button_neg.grid(row=4, column=3)
        self.button_equal.grid(row=4, column=4)

        self.f_num = 0
        self.math = ""

    # button click
    def button_click(self, number):
        current = self.number_entry.get()
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, str(current) + str(number))

    # Clear
    def button_clear(self):
        self.number_entry.delete(0, tk.END)

    #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

    # +
    def button_add(self):
        first_number = self.number_entry.get()
        self.math = "addition"
        self.f_num = int(first_number)
        self.number_entry.delete(0, tk.END)

    # =
    def button_equal(self):
        second_number = self.number_entry.get()
        self.number_entry.delete(0, tk.END)

        if self.math == "addition":
            self.number_entry.insert(0, self.f_num + int(second_number))

        if self.math == "multiplication":
            self.number_entry.insert(0, self.f_num * int(second_number))

        if self.math == "division":
            if int(second_number) != 0:
                self.number_entry.insert(0, self.f_num / int(second_number))
            else:
                self.number_entry.insert(0, "Ошибка")

        if self.math == "floor_div":
            self.number_entry.insert(0, self.f_num // int(second_number))

        if self.math == "modulus":
            self.number_entry.insert(0, self.f_num % int(second_number))

    # -
    def button_subtract(self):
        first_number = self.number_entry.get()
        self.math = "subtraction"
        self.f_num = int(first_number)
        self.number_entry.delete(0, tk.END)

    # *
    def button_multiply(self):
        first_number = self.number_entry.get()
        self.math = "multiplication"
        self.f_num = int(first_number)
        self.number_entry.delete(0, tk.END)

    # /
    def button_divide(self):
        first_number = self.number_entry.get()
        self.math = "division"
        self.f_num = int(first_number)
        self.number_entry.delete(0, tk.END)

    # //
    def button_floor_div(self):
        first_number = self.number_entry.get()
        try:
            self.math = "floor_div"
            self.f_num = int(first_number)
            self.number_entry.delete(0, tk.END)

        except ZeroDivisionError as e:
            self.number_entry.insert(0, f'{e}')

    # %
    def button_modulus(self):
        first_number = self.number_entry.get()
        self.math = "modulus"
        self.f_num = int(first_number)
        self.number_entry.delete(0, tk.END)

    # **2
    def button_sqrt(self):
        if self.number_entry.get().startswith("-"):
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, 'RuntimeError')

        else:
            number = float(self.number_entry.get())
            result = sqrt(number)
            if result.is_integer():
                self.number_entry.delete(0, tk.END)
                self.number_entry.insert(0, int(result))
            else:
                self.number_entry.delete(0, tk.END)
                self.number_entry.insert(0, result)

    # -n
    def button_neg(self):
        current = self.number_entry.get()
        if current.startswith("-"):
            current = current[1:]
        else:
            current = "-" + current
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, current)


if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
