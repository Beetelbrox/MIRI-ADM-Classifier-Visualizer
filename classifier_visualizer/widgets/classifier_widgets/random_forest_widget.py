import tkinter as tk
from .classifier_widget import ClassifierWidget
from widgets.slider_widget import SliderWidget
from sklearn.ensemble import RandomForestClassifier

class RandomForestWidget(ClassifierWidget):
    CLASSIFIER_NAME = "Random Forest"
    CLASSIFIER_FUNCTION = RandomForestClassifier

    def __init__(self, master, initial_max_depth=5, initial_num_estimators=10):
        super().__init__(master, self.CLASSIFIER_NAME)
        self.max_depth_val_slider = SliderWidget(self, "Max depth", min_val=1, max_val=32, initial_value=initial_max_depth)
        self.num_estimators_val_slider = SliderWidget(self, "Num estimators", min_val=1, max_val=32, initial_value=initial_num_estimators)
    
    def get_classifier(self):
        return self.CLASSIFIER_FUNCTION(
            max_depth=self.max_depth_val_slider.get_value(),
            n_estimators=self.num_estimators_val_slider.get_value(),
            max_features=1)