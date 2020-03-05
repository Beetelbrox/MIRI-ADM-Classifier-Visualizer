import tkinter as tk
from .classifier_widget import ClassifierWidget
from sklearn.ensemble import AdaBoostClassifier

class AdaBoostWidget(ClassifierWidget):
    CLASSIFIER_NAME = "AdaBoost"
    CLASSIFIER_FUNCTION = AdaBoostClassifier

    def __init__(self, master):
        super().__init__(master, self.CLASSIFIER_NAME)
        t = tk.Label(self, text="No parameters required for AdaBoost!")
        t.pack()
    
    def get_classifier(self):
        return self.CLASSIFIER_FUNCTION()