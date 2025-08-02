import tkinter as tk

def press(val):
    old = display.get()
    display.delete(0, tk.END)
    display.insert(0, old + val)

def calculate():
    try:
        expr = display.get()
        output = str(eval(expr))
        display.delete(0, tk.END)
        display.insert(0, output)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def clear():
    display.delete(0, tk.END)

def backspace():
    now = display.get()
    if now:
        display.delete(0, tk.END)
        display.insert(0, now[:-1])

win = tk.Tk()
win.title("Calculator")
win.resizable(False, False)

display = tk.Entry(win)
display["font"] = ("Arial", 18)
display["width"] = 22
display["bd"] = 5
display["relief"] = "sunken"
display.pack(padx=10, pady=10)

buttons = [
    ['AC', '←', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['()', '0', '.', '=']
]

for row in buttons:
    box = tk.Frame(master=win)
    box.pack()
    for label in row:
        b = tk.Button(master=box)
        b["text"] = label
        b["width"] = 5
        b["height"] = 2
        b["font"] = ("Arial", 14)
        if label == 'AC':
            b["command"] = clear
        elif label == '←':
            b["command"] = backspace
        elif label == '=':
            b["command"] = calculate
        elif label == '()':
            b["command"] = lambda: press('()')  # or you can implement smart parens logic
        else:
            b["command"] = lambda x=label: press(x)
        b.pack(side="left", padx=3, pady=3)

win.mainloop()
