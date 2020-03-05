import tkinter as tk

class TextInputWidget(tk.Frame):

    def __init__(self, master, label, initial_value):
        super().__init__(master)
        self.pack(side=tk.TOP, fill=tk.X, padx=4, pady=2)
        self.text_val = tk.StringVar(self)
        self.text_val.set(initial_value)

        label = tk.Label(self, text=label, anchor='w')
        label.pack(side=tk.LEFT)
        text_field = tk.Entry(self, textvariable=self.text_val)
        text_field.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X, padx=2)
    
    def get_value(self):
        return self.text_val.get()

