#!/usr/bin/env python3

import tkinter as tk
from display import Display
from input_area import InputArea
import numpy.random as rd
import numpy as np

class ClassifierVisualizer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.title("Classifier Visualizer Tool - v 0.2")
        self.display_width = 500
        self.display_height = 500
        self.display=Display(self, self.display_width, self.display_height)
        self.display.pack(side = tk.RIGHT, fill=tk.NONE)
        self.input_area = InputArea(self)
        self.input_area.pack(side = tk.LEFT, fill=tk.BOTH)

        self.points = None
    
    def run_classifier(self, classifier):
        print(classifier)
    
    def generate_points_at(self, x, y, c):
        distribution = self.input_area.data_widget.manual_data_widget.get_distribution()
        num_points = self.input_area.data_widget.manual_data_widget.get_num_points()
        dispersion = self.input_area.data_widget.manual_data_widget.get_dispersion()
        if distribution == "Uniform":
            points = self.generate_points_uniform(x, y, num_points, dispersion, c)
        elif distribution == "Gaussian":
            points = self.generate_points_gaussian(x, y, num_points, dispersion, c)
        self.points = points if self.points is None else np.append(self.points, points, axis=0)
        for x, y, c in points: self.display.draw_point(x,y,1,c)

    
    def generate_points_uniform(self, x, y, n, r, c):
        rand_radius = rd.uniform(size=n)
        rand_theta = rd.uniform(size=n)*2*np.pi
        rand_x =  x + r*np.sqrt(rand_radius)*np.cos(rand_theta)
        rand_y =  y + r*np.sqrt(rand_radius)*np.sin(rand_theta)
        labels = np.full(shape=n, fill_value=c)
        return np.stack((rand_x, rand_y, labels), axis=-1)

    def generate_points_gaussian(self, x, y, n, sigma, c):
        rand_x = rd.normal(loc=x, scale=sigma, size=n)
        rand_y = rd.normal(loc=y, scale=sigma, size=n)
        labels = np.full(shape=n, fill_value=c)
        return np.stack((rand_x, rand_y, labels), axis=-1)
    


root = tk.Tk()
app = ClassifierVisualizer(root)
app.mainloop()