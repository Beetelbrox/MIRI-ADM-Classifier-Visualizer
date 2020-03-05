import tkinter as tk
from widgets.slider_widget import SliderWidget
from widgets.dropdown_widget import DropdownWidget

class ManualDataWidget(tk.Frame):

    DISTRIBUTIONS = []
    def __init__(self, master, initial_num_points=200, initial_dispersion=50):
        super().__init__(master)
        config_label = tk.Label(self, width=33, text="Manual", anchor="w")
        config_label.pack()
        self.distribution_dropdown = DropdownWidget( self, "Distribution", ["Uniform", "Gaussian"])
        self.num_points_slider = SliderWidget(self, "Number of Points", min_val=1, max_val=500, initial_value=initial_num_points)
        self.dispersion_slider = SliderWidget(self, "Dispersion", min_val=1, max_val=200, initial_value=initial_dispersion)
        

    def get_distribution(self):
        return self.distribution_dropdown.get_value()
    
    def get_num_points (self):
        return self.num_points_slider.get_value()
    
    def get_dispersion(self):
        return self.dispersion_slider.get_value()