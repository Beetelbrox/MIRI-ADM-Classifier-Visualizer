import tkinter as tk
from .classifier_widget import ClassifierWidget
from sklearn.svm import SVC
from widgets.text_input_widget import TextInputWidget


class SVMLinearWidget(ClassifierWidget):
    CLASSIFIER_NAME = "SVM (Linear kernel)"
    CLASSIFIER_FUNCTION = SVC

    def __init__(self, master, initial_c_value=0.025):
        super().__init__(master, self.CLASSIFIER_NAME)
        self.c_val_textfield = TextInputWidget(self, "C", initial_value=initial_c_value)

    def get_classifier(self):
        return self.CLASSIFIER_FUNCTION(kernel="linear", C=self.c_val_textfield.get_value())