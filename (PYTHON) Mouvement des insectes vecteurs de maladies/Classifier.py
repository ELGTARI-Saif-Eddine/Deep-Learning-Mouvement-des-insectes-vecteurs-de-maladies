import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix



class SvmClassifier(object):
    
    def __init__(self,path,file_name):
        super(SvmClassifier, self).__init__()
        
        print('Start Train')
        print('...')
        
        self.data = pd.read_csv(path + file_name)
        X = self.data.drop('Class', axis=1)
        y = self.data['Class']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
        self.svclassifier = SVC(kernel='rbf')
        self.svclassifier.fit(X_train, y_train)
               
        print("Training finished")
        
    def __del__(self): 
        del self.svclassifier
 
 
    def classify(self,phi):
        
        y_pred = self.svclassifier.predict(phi)
        return y_pred












