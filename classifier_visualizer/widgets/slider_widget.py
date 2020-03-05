import tkinter as tk

class SliderWidget(tk.Frame):

    def __init__( self, master, label, min_val, max_val, initial_value, scale_resolution=1 ):
        super().__init__(master)
        self.master = master
        self.pack(side=tk.TOP, fill=tk.X, padx=4, pady=2)
        self.slider_val = tk.IntVar(self)
        self.slider_val.set(initial_value)

        slider_label = tk.Label(self, text=label, anchor="w")
        slider_label.pack(side=tk.LEFT)
        scale = tk.Scale(self, from_=min_val, to=max_val, resolution=scale_resolution, orient=tk.HORIZONTAL, showvalue=False, variable=self.slider_val)
        scale.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X, padx=2)
        slider_value_label = tk.Label(self, textvariable=self.slider_val, width=3, anchor="w")
        slider_value_label.pack(side=tk.LEFT)
        
    def get_value(self):
        return self.slider_val.get()
