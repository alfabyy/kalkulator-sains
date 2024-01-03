import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator Sains")

        self.style = Style(theme="minty")
        self.style.configure('TButton', font=('Arial', 12))
        self.style.configure('Equals.TButton', background='orange')

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = ttk.Frame(self, padding="20")
        self.main_frame.grid(row=0, column=0)

        self.entry = ttk.Entry(self.main_frame, font=('Arial', 18))
        self.entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="ew")

        button_values = [
            ('7', '8', '9', '/', 'sqrt'),
            ('4', '5', '6', '*', 'kuadrat'),
            ('1', '2', '3', '-', 'cos'),
            ('.', '0', '=', '+', 'sin'),
            ('C', 'DEL', '(', ')', 'tan'),
            ('log', 'exp', 'mod', '', ''),
        ]

        for i, row in enumerate(button_values):
            for j, value in enumerate(row):
                if value == '=':
                    button = ttk.Button(self.main_frame, text=value, command=self.calculate, style='Equals.TButton')
                elif value == 'C':
                    button = ttk.Button(self.main_frame, text=value, command=self.clear_entry)
                elif value == 'DEL':
                    button = ttk.Button(self.main_frame, text=value, command=self.delete_last)
                elif value == 'sqrt':
                    button = ttk.Button(self.main_frame, text=value, command=self.sqrt)
                elif value == 'sin':
                    button = ttk.Button(self.main_frame, text=value, command=self.sin)
                elif value == 'cos':
                    button = ttk.Button(self.main_frame, text=value, command=self.cos)
                elif value == 'tan':
                    button = ttk.Button(self.main_frame, text=value, command=self.tan)
                elif value == 'kuadrat':
                    button = ttk.Button(self.main_frame, text='x^2', command=self.kuadrat)
                elif value == 'log':
                    button = ttk.Button(self.main_frame, text=value, command=self.logarithm)
                elif value == 'exp':
                    button = ttk.Button(self.main_frame, text='exp', command=self.exponent)
                elif value == 'mod':
                    button = ttk.Button(self.main_frame, text=value, command=self.modulus)
                else:
                    button = ttk.Button(self.main_frame, text=value, command=lambda v=value: self.append_to_entry(v))
                button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def append_to_entry(self, value):
        self.entry.insert(tk.END, value)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def delete_last(self):
        self.entry.delete(len(self.entry.get()) - 1, tk.END)

    def sqrt(self):
        try:
            result = math.sqrt(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def sin(self):
        try:
            result = math.sin(math.radians(eval(self.entry.get())))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def cos(self):
        try:
            result = math.cos(math.radians(eval(self.entry.get())))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def tan(self):
        try:
            result = math.tan(math.radians(eval(self.entry.get())))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def kuadrat(self):
        try:
            result = eval(self.entry.get()) ** 2
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def logarithm(self):
        try:
            expression = self.entry.get()
            if '^' in expression:  
                base, value = expression.split('^')  
                result = math.log(float(value), float(base)) 
            else:
                result = math.log(float(expression)) 

            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")



    def exponent(self):
        try:
            result = math.exp(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def modulus(self):
        try:
            result = math.modf(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
