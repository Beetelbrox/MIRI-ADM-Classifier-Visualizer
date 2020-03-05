import tkinter as tk
from tkinter import ttk
from .manual_data_widget import ManualDataWidget
from .auto_data_widget import AutoDataWidget


class DataWidget(tk.Frame):

    def __init__(self, master):
        super().__init__(master, highlightbackground="gray",highlightthickness=1)
        self.tabs = ttk.Notebook(self)
        self.tabs.pack()
        self.manual_data_widget = ManualDataWidget(self)
        self.auto_data_widget = AutoDataWidget(self)
        self.tabs.add(self.manual_data_widget, text="Manual")
        self.tabs.add(self.auto_data_widget, text="Auto")

