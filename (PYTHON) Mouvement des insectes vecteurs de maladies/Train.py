
from InsectsTrack import InsectsTrack 
from SaveDataToCSV import SaveDataToCSV
import numpy as np
import time


class Train(object):
    
    def __init__(self,path,video_list):
        super(Train, self).__init__()
        
        self.insectsTrack = InsectsTrack()
        self.globl = self.insectsTrack.getGlobalClass()
      
        self.path= path #'C:\\'
        self.db_video= video_list #['GOPR0011_2.avi']
        
        self.dataFrame= [[] for i in range(len(video_list))]
        self.totalDataFrame = []
    
          

    def startCollectingData(self):
        i=0
        while(i<len(self.db_video)):
            
            print("\nStart collecting attributes from Video number {}".format(i+1))
            print("...")
            
            self.globl.setVideoName(self.path, self.db_video[i])
            self.dataFrame[i]=self.insectsTrack.collectAtributestoDB()
            #self.totalDataFrame.append(self.insectsTrack.collectAtributestoDB())
            
            print(self.dataFrame[i])
            
            time.sleep(1)
            i=i+1
        
        print("\n")
        print("Saving data ...")
        self.saveDataToCSV.save(path=self.path, data=self.totalDataFrame) 
        print(" 'Data.csv' saved successfully in that folder: {}".format(self.path)) 


        
        



