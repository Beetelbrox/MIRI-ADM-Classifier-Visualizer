import tkinter as tk
from .classifier_widget import ClassifierWidget
from widgets.slider_widget import SliderWidget
from sklearn.tree import DecisionTreeClassifier

class DecisionTreeWidget(ClassifierWidget):
    CLASSIFIER_NAME = "Decision Tree"
    CLASSIFIER_FUNCTION = DecisionTreeClassifier

    def __init__(self, master, max_depth=5):
        super().__init__(master, self.CLASSIFIER_NAME)
        self.max_depth_val_slider = SliderWidget(self, "Max tree depth", min_val=1, max_val=32, initial_value=max_depth)
    
    def get_classifier(self):
        return self.CLASSIFIER_FUNCTION(max_depth=self.max_depth_val_slider.get_value())