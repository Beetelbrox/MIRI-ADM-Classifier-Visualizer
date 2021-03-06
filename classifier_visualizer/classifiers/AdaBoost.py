from sklearn.ensemble import AdaBoostClassifier

def createModel(parameters, trainData, trainLabel):
    model = AdaBoostClassifier()
    model.fit(trainData, trainLabel)
    return model
