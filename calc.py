import tkinter as tk
import math

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def cal():
    try: 
        exp = entry.get()
        exp = exp.replace('^', '**')
        exp = exp.replace('√', 'math.sqrt')
        exp = exp.replace('sin', 'math.sin(math.radians')
        exp = exp.replace('cos', 'math.cos(math.radians')
        exp = exp.replace('tan', 'math.tan(math.radians')
        exp = exp.replace('sec', '(1/math.cos(math.radians')
        exp = exp.replace('csc', '(1/math.sin(math.radians')
        exp = exp.replace('cot', '(1/math.tan(math.radians')
        exp = exp.replace(')', '))')

        result = eval(exp)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="black")
root.resizable(False, False)

entry = tk.Entry(root, font=("Segoe UI", 20),
                 bg='#2d2d2d', fg='white',
                 bd=0, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

buttons = [
    'sin', 'cos', 'tan','sec', 
    'cos', 'cot', 'csc','^',
     '(', ')', '√','%',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

r, c = 1, 0
for b in buttons:
    cmd = cal if b == '=' else lambda x=b: press(x)
    tk.Button(
        root, text=b, command=cmd,
        width=5, height=2,
        font=('Segoe UI', 14),
        bg='#ff9500' if b in '=+-*/' else '#3a3a3a',
        fg='white', bd=0
    ).grid(row=r, column=c, padx=6, pady=6)

    c += 1
    if c == 4:
        c = 0
        r += 1

tk.Button(
    root, text='C', command=clear,
    font=('Segoe UI', 14),
    bg='#ff3b3b', fg='white',
    bd=0, width=22, height=2
).grid(row=r, column=0, columnspan=4, padx=6, pady=8)

root.mainloop()
