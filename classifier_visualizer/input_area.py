import tkinter as tk
from widgets.config_widget import ConfigWidget
from widgets.dropdown_widget import DropdownWidget
from widgets.data_widget import DataWidget
from widgets.classifier_widgets import *



class InputArea(tk.Frame):

    AVAILABLE_CLASSIFIER_WIDGETS = [KNNWidget, NaiveBayesWidget, DecisionTreeWidget, AdaBoostWidget, RandomForestWidget,
        SVMLinearWidget, SVMRBFWidget, MLPWidget]

    def __init__(self, master):
        super().__init__(master, highlightbackground="gray",highlightthickness=1)
        self.master = master
        self.config_widget = ConfigWidget(self)
        self.config_widget.pack(side=tk.TOP, fill=tk.X)
        self.classifier_widget_container = tk.Frame(self, highlightbackground="gray",highlightthickness=1)
        self.classifier_widget_container.pack(side=tk.TOP, fill=tk.X)
        self.classifier_widgets = { c.CLASSIFIER_NAME : c(self.classifier_widget_container) for c in self.AVAILABLE_CLASSIFIER_WIDGETS}
        self.classifier_dropdown = DropdownWidget(
            self.classifier_widget_container,
            "Classifier",
            [c.CLASSIFIER_NAME for c in self.AVAILABLE_CLASSIFIER_WIDGETS],
            callback=self.classifier_selection_callback)
        self.current_classifier_widget = self.classifier_widgets[self.classifier_dropdown.get_value()]
        self.current_classifier_widget.pack(side=tk.TOP, fill=tk.X, pady=2)
        self.data_widget = DataWidget(self)
        self.data_widget.pack()

        self.classify_button = tk.Button(self, text="Run classifier!", command=self.run_classifier, anchor='s')
        self.classify_button.pack(side=tk.BOTTOM, fill=tk.X)
        
    def classifier_selection_callback(self, selected_classifier):
        if selected_classifier != self.current_classifier_widget.CLASSIFIER_NAME:
            self.current_classifier_widget.pack_forget()
            self.current_classifier_widget = self.classifier_widgets[selected_classifier]
            self.current_classifier_widget.pack(side=tk.TOP, fill=tk.X, pady=2)

    def run_classifier(self):
        self.master.run_classifier(self.current_classifier_widget.get_classifier())