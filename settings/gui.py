import tkinter as tk
from tkinter import Button, ttk
from tkinter.colorchooser import askcolor

class SettingsModule(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.font = ("Arial", 15)

        self.create_test_label()
    
    def create_test_label(self):
        self.test_label = tk.Label(self, text="Settings", font=self.font)
        self.test_label.grid(row=0, column=0)

    def change_color(self):
        colors = askcolor(title="Tkinter Color Chooser")
        self.configure(bg=colors[1])
        

    def color_button(self):
        self.button = ttk.Button(
        text='Select a Color',
        command=self.change_color).pack(expand=True)
        self.test_label.grid(row=1, column=1)    
