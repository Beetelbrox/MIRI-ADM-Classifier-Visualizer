import tkinter as tk
from .classifier_widget import ClassifierWidget
from sklearn.naive_bayes import GaussianNB

class NaiveBayesWidget(ClassifierWidget):
    CLASSIFIER_NAME = "Naive Bayes"
    CLASSIFIER_FUNCTION = GaussianNB

    def __init__(self, master):
        super().__init__(master, self.CLASSIFIER_NAME)
        t = tk.Label(self, text="No parameters required for naive Bayes!")
        t.pack()
    
    def get_classifier(self):
        return GaussianNB()