import tkinter as tk
from .classifier_widget import ClassifierWidget
from widgets.slider_widget import SliderWidget
from sklearn.neural_network import MLPClassifier

class MLPWidget(ClassifierWidget):
    CLASSIFIER_NAME = "Multi-Layer Perceptron"
    CLASSIFIER_FUNCTION = MLPClassifier

    def __init__(self, master, initial_num_hidden_layers=3, initial_num_neurons_layer=10):
        super().__init__(master, self.CLASSIFIER_NAME)
        self.num_hidden_layers_val_slider = SliderWidget(self, "Hidden layers", min_val=1, max_val=10, initial_value=initial_num_hidden_layers)
        self.num_neurons_layer_val_slider = SliderWidget(self, "Neurons/Layer", min_val=1, max_val=100, initial_value=initial_num_neurons_layer)
    
    def get_classifier(self):
        hidden_layer_sizes = tuple([self.num_neurons_layer_val_slider.get_value()]*self.num_neurons_layer_val_slider.get_value())
        return self.CLASSIFIER_FUNCTION(hidden_layer_sizes=hidden_layer_sizes, max_iter=500)