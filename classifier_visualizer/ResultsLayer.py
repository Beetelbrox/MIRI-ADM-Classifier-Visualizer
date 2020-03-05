import tkinter
import tkinter.messagebox
from tkinter import ttk
import Classifiers 
from MyCanvas import *

# All logic related to the results to show
class ResultsLayer():
    def __init__(self, GUI, parentFrame):
        self.GUI = GUI

        titleFrame = tkinter.Frame(parentFrame)
        titleFrame.pack()
        lab = tkinter.Label(titleFrame, width=30, text="Results", anchor='center')
        lab.pack(side=tkinter.LEFT)


        resultsFrame = tkinter.Frame(parentFrame)
        resultsFrame.pack()

        testFrame = tkinter.LabelFrame(resultsFrame, text='Test Points')
        testFrame.pack(padx= 5)
        
        (_,self.testPointsLabel) = self.makeLabelform(testFrame, 'Num test points', '-')
        (_,self.testcorrectLabel) = self.makeLabelform(testFrame, 'Correct predictions', '-')
        
        (_,self.testwrongLabel) = self.makeLabelform(testFrame, 'Wrong predictions', '-')
        (_,self.accuracyLabel) = self.makeLabelform(testFrame, 'Accuracy (%)', '-')
        (_,self.incorrectAccuracyLabel) = self.makeLabelform(testFrame, 'Incorrect prediction (%)', '-')

        trainFrame = tkinter.LabelFrame(resultsFrame, text='Train Points')
        trainFrame.pack(padx= 5)
        (_,self.trainPointsLabel) = self.makeLabelform(trainFrame, 'Num train points', '-')
        (_,self.traincorrectLabel) = self.makeLabelform(trainFrame, 'Correct predictions', '-')
        
        (_,self.trainwrongLabel) = self.makeLabelform(trainFrame, 'Wrong predictions', '-')
        (_,self.accuracyTrainLabel) = self.makeLabelform(trainFrame, 'Accuracy (%)', '-')
        (_,self.incorrectAccuracyTrainLabel) = self.makeLabelform(trainFrame, 'Incorrect prediction (%)', '-')

    def updateTrainTestRatio(self, event):
        print(event) 

    def makeLabelform(self, root, field, value):
        row = tkinter.Frame(root)
        lab = tkinter.Label(row, width=20, text=field, anchor='e')
        ent = tkinter.Label(row,text= value, width = 10)
        row.pack(side=tkinter.TOP, fill=tkinter.X, padx=0, pady=5)
        lab.pack(side=tkinter.LEFT)
        ent.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.X)
        return (row,ent)

    def updateResults(self, nTraining, nTesting, correctPredictionTraining, correctPredictionTesting):
        testAcc = 100*float(correctPredictionTesting)/float(nTesting)
        self.accuracyLabel['text'] = str(round(testAcc,2)) + '%'
        self.incorrectAccuracyLabel['text'] = str(round(100-testAcc,2)) + '%'
        self.testPointsLabel['text'] = str(nTesting)
        self.testcorrectLabel['text'] = str(correctPredictionTesting)
        self.testwrongLabel['text'] = str(nTesting - correctPredictionTesting)
        
        trainAcc = 100*float(correctPredictionTraining)/float(nTraining)
        self.accuracyTrainLabel['text'] = str(round(trainAcc,2)) + '%'
        self.incorrectAccuracyTrainLabel['text'] = str(round(100-trainAcc,2)) + '%'
        self.trainPointsLabel['text'] = str(nTraining)
        
        self.traincorrectLabel['text'] = str(correctPredictionTraining)
        self.trainwrongLabel['text'] = str(nTraining - correctPredictionTraining)
