import tkinter as tk

class DropdownWidget(tk.Frame):

    def __init__(self, master, label, value_list, initial_value=None, callback=None):
        super().__init__(master)
        self.master=master
        self.pack(side=tk.TOP, fill=tk.X, padx=4, pady=6)
        self.dropdown_val = tk.StringVar(self)
        self.dropdown_val.set(value_list[0] if initial_value is None else initial_value)
        dropdown_label = tk.Label(self, text=label, anchor="w")

        dropdown_label.pack(side=tk.LEFT)
        classifier_dropdown = tk.OptionMenu(self, self.dropdown_val, *value_list, command=callback)
        classifier_dropdown.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=4)
    
    def get_value(self):
        return self.dropdown_val.get()
