import tkinter as tk
from .classifier_widget import ClassifierWidget
from sklearn.svm import SVC
from widgets.text_input_widget import TextInputWidget

class SVMRBFWidget(ClassifierWidget):
    CLASSIFIER_NAME = "SVM (RBF kernel)"
    CLASSIFIER_FUNCTION = SVC

    def __init__(self, master, initial_c_value=1, initial_gamma_value=2):
        super().__init__(master, self.CLASSIFIER_NAME)
        self.c_val_textfield = TextInputWidget(self, "C", initial_value=initial_c_value)
        self.gamma_val_textfield = TextInputWidget(self, "Gamma", initial_value=initial_gamma_value)
    
    def get_classifier(self):
        return self.CLASSIFIER_FUNCTION(gamma=self.gamma_val_textfield.get_value(), C=self.c_val_textfield.get_value())