import tkinter as tk
from .classifier_widget import ClassifierWidget
from widgets.slider_widget import SliderWidget
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class KNNWidget(ClassifierWidget):
    CLASSIFIER_NAME = "k-Nearest Neighbours"
    CLASSIFIER_FUNCTION = KNeighborsClassifier

    def __init__(self, master, k=3):
        super().__init__(master, self.CLASSIFIER_NAME)
        self.k_val_slider = SliderWidget(self, "k", min_val=1, max_val=32, initial_value=k)
    
    def get_classifier(self):
        return self.CLASSIFIER_FUNCTION(n_neighbors=self.k_val_slider.get_value())