import tkinter as tk
import os

task_file = "tasks.txt"
task_data = []

def load_from_file():
    if os.path.exists(task_file):
        with open(task_file, "r") as f:
            lines = f.readlines()
            for l in lines:
                txt = l.strip()
                if txt:
                    task_data.append(txt)
    update_task_list()

def save_to_file():
    with open(task_file, "w") as f:
        for t in task_data:
            f.write(t + "\n")

def update_task_list():
    task_list.delete(0, tk.END)
    for idx in range(len(task_data)):
        line = str(idx + 1) + ". " + task_data[idx]
        task_list.insert(tk.END, line)

def add_task():
    new_text = input_field.get()
    if new_text != "":
        task_data.append(new_text)
        input_field.delete(0, tk.END)
        save_to_file()
        update_task_list()

def delete_selected():
    selected = task_list.curselection()
    if selected:
        i = selected[0]
        task_data.pop(i)
        save_to_file()
        update_task_list()

def delete_all():
    task_data.clear()
    save_to_file()
    update_task_list()

# GUI setup
window = tk.Tk()
window.title("To-Do List")

top_section = tk.Frame(master=window)
top_section.pack(pady=10)

input_field = tk.Entry(master=top_section)
input_field["width"] = 35
input_field.pack(side="left", padx=(0, 5))

button_add = tk.Button(master=top_section)
button_add["text"] = "Add"
button_add["command"] = add_task
button_add.pack(side="left")

task_list = tk.Listbox(master=window)
task_list["width"] = 50
task_list["height"] = 10
task_list.pack(pady=10)

button_row = tk.Frame(master=window)
button_row.pack(pady=5)

button_delete = tk.Button(master=button_row)
button_delete["text"] = "Delete Selected"
button_delete["command"] = delete_selected
button_delete.pack(side="left", padx=5)

button_clear = tk.Button(master=button_row)
button_clear["text"] = "Delete All"
button_clear["command"] = delete_all
button_clear.pack(side="left", padx=5)

load_from_file()
window.mainloop()
