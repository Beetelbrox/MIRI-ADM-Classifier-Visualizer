import tkinter as tk

class AutoDataWidget(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        config_label = tk.Label(self, width=33, text="Auto", anchor="w")
        config_label.pack()