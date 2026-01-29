from tkinter import filedialog
import tkinter as tk

def choose_file(entry):
    file_name = filedialog.askopenfilename()
    if file_name:
        entry.delete(0, tk.END)
        entry.insert(0, file_name)

def choose_dir(entry):
    dir_name = filedialog.askdirectory()
    if dir_name:
        entry.delete(0, tk.END)
        entry.insert(0, dir_name)