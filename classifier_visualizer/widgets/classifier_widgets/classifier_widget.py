import tkinter as tk

class ClassifierWidget(tk.Frame):

    def __init__(self, master, classifier_name):
        super().__init__(master)
        self.master =  master
        self.classifier_name = classifier_name
    
    def get_classifier(self):
        return None
    