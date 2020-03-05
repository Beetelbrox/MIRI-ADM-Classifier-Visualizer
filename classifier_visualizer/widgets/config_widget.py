import tkinter as tk
from widgets.slider_widget import SliderWidget

class ConfigWidget(tk.Frame):

    INITIAL_TT_RATIO=70
    def __init__(self, master):
        super().__init__(master, highlightbackground="gray",highlightthickness=1)
        self.master =  master
        config_label = tk.Label(self, width=33, text="General", anchor="w")
        config_label.pack(side=tk.TOP)
        self.train_test_slider = SliderWidget(self, "Train/Test ratio", min_val=1, max_val=99, initial_value=self.INITIAL_TT_RATIO)
    
    def get_train_test_ratio(self):
        return self.train_test_slider.get_value()
