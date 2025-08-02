import tkinter as tk
import random
import string

def make():
    val = length_field.get()
    if val.isdigit():
        total = int(val)
        if total >= 4:
            l = random.choice(string.ascii_lowercase)
            u = random.choice(string.ascii_uppercase)
            d = random.choice(string.digits)
            s = random.choice("!@#$%^&*")
            mix = string.ascii_letters + string.digits + "!@#$%^&*"
            rest = random.choices(mix, k=total - 4)
            all_parts = [l, u, d, s] + rest
            random.shuffle(all_parts)
            final = ''.join(all_parts)
            result.delete(0, tk.END)
            result.insert(0, final)
            note["text"] = ""
        else:
            result.delete(0, tk.END)
            result.insert(0, "Minimum is 4")
            note["text"] = ""
    else:
        result.delete(0, tk.END)
        result.insert(0, "Enter number")
        note["text"] = ""

def copy_now():
    txt = result.get()
    if txt:
        root.clipboard_clear()
        root.clipboard_append(txt)
        note["text"] = "Copied to clipboard"

root = tk.Tk()
root.title("Password Maker")
root.geometry("320x210")
root.resizable(False, False)

top = tk.Frame(root)
top.pack(pady=10)

tk.Label(top, text="Length:").pack(side="left")
length_field = tk.Entry(top, width=6)
length_field.pack(side="left", padx=10)

gen = tk.Button(top, text="Generate", command=make)
gen.pack(side="left")

middle = tk.Frame(root)
middle.pack(pady=10)

result = tk.Entry(middle, width=28, font=("Arial", 12))
result.pack(side="left", padx=(0, 5))

copy_btn = tk.Button(middle, text="Copy", command=copy_now)
copy_btn.pack(side="left")

note = tk.Label(root, text="", fg="green")
note.pack(pady=(5, 0))

root.mainloop()
