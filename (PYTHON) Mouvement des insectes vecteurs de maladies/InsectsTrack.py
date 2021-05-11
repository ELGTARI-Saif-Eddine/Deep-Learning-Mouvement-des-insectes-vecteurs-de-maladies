import numpy as np 
import cv2
from tracker import Tracker
from InsectsDetector import InsectsSubtractor
from Attributes import AttributePhi
from Global import Global

import time
import imageio
import numpy
images = []


import matplotlib.pyplot as plt


class InsectsTrack(object):
    
    def __init__(self):
        super(InsectsTrack, self).__init__()
        self.globl=Global()
        
        self.insects=InsectsSubtractor(self.globl)
        self.attribut = AttributePhi()

        
        self.tracker = Tracker(150, 30, 5)
        self.track_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                             (127, 127, 255), (255, 0, 255), (255, 127, 255),
                             (127, 0, 255), (127, 0, 127),(127, 10, 255), (0,255, 127)]
 
    
    def __del__(self): 
        self.track_colors.clear()
        del self.insects
 
 

    def track(self, classifier):
 
        newData=[[] for i in range(50)]
        dataPhiAttribute=[[] for i in range(50)]
        i=0 
      
        print(" ".format(self.insects.getNumberOfFrames()) )
      
        while(i<self.insects.getNumberOfFrames()):

            centers = self.insects.getInsectsCoordinates()
            oldData=centers
            frame = self.insects.getActualFrame()  #createimage(720,1280)
            if (len(centers) > 0):
                self.tracker.update(centers)

                       
                for j in range(len(self.tracker.tracks)):
                    if (len(self.tracker.tracks[j].trace) > 1):
                    
                        x = numpy.abs(int(self.tracker.tracks[j].trace[-1][0,0]))
                        y = numpy.abs(int(self.tracker.tracks[j].trace[-1][0,1]))

                        newData[self.tracker.tracks[j].trackId].append(numpy.abs([x,y]))
                        
                        tl = (x-12,y-12)
                        br = (x+12,y+12)
                        #cv2.rectangle(frame,tl,br,self.track_colors[j],1)
                        #cv2.putText(frame,str(self.tracker.tracks[j].trackId + 1), (x-10,y-20),0, 0.5, self.track_colors[j],2)
                        for k in range(len(self.tracker.tracks[j].trace)):
                            x = int(self.tracker.tracks[j].trace[k][0,0])
                            y = int(self.tracker.tracks[j].trace[k][0,1])
                            #cv2.circle(frame,(x,y), 2, self.track_colors[j],-2)

                    try:
                        if(len(newData[0])>1):
                            dataPhiAttribute[self.tracker.tracks[j].trackId].append(self.attribut.phi( x1=newData[self.tracker.tracks[j].trackId][len(newData[self.tracker.tracks[j].trackId])-1][0], 
                                                                                             x0=newData[self.tracker.tracks[j].trackId][len(newData[self.tracker.tracks[j].trackId])-2][0],
                                                                                             y1=newData[self.tracker.tracks[j].trackId][len(newData[self.tracker.tracks[j].trackId])-1][1],
                                                                                             y0=newData[self.tracker.tracks[j].trackId][len(newData[self.tracker.tracks[j].trackId])-2][1]))
                   
                        if(len(self.attribut.Teta)>1): 
                            print("Phi_"+repr(j+1)+" = " + repr(dataPhiAttribute[self.tracker.tracks[j].trackId][len(dataPhiAttribute[self.tracker.tracks[j].trackId])-1]))
                            
                            ''' ToDo add classifier '''
                            y=classifier.classify(dataPhiAttribute[self.tracker.tracks[j].trackId])
                            #print(y)                    
                    except:
                        error=1
                        print('ERROR 2')
                #print(len(newData))
                try:
                    cv2.imshow('image',frame)
                except:
                    print("\n-------- Track finished---------\n")  
                    #saveDataToCSV.save(dataPhiAttribute)
                    break
                print("---------------------------------------------------------------")
                i=i+1
                
            #Sleep time between frames
                #****time.sleep(0.1)
                
                ##########################################
                #
                #     Press 'q' button to quit track
                #
                ##########################################
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("\n-------- Quit Track ---------\n")
                    cv2.destroyAllWindows()
                    break
               




    def collectAtributestoDB(self):
 
        newData=[]
        dataPhiAttribute=[]
        i=0 
                        
        self.insects.initialization()     
        self.tracker = Tracker(150, 30, 5)
        
        
        
        
        while(i<self.insects.getNumberOfFrames()):
            
            frame = self.insects.getActualFrame()  #createimage(720,1280)
            centers = self.insects.getInsectsCoordinates()
            oldData=centers
            
            
            if (len(centers) > 0):
                self.tracker.update(centers)
      
                for j in range(len(self.tracker.tracks)):
                    if (len(self.tracker.tracks[j].trace) > 1):
                    
                        x = numpy.abs(int(self.tracker.tracks[j].trace[-1][0,0]))
                        y = numpy.abs(int(self.tracker.tracks[j].trace[-1][0,1]))

                        newData.append(numpy.abs([x,y]))
                        
                        tl = (x-12,y-12)
                        br = (x+12,y+12)
                        cv2.rectangle(frame,tl,br,self.track_colors[j],1)
                        cv2.putText(frame,str(self.tracker.tracks[j].trackId + 1), (x-10,y-20),0, 0.5, self.track_colors[j],2)
                        for k in range(len(self.tracker.tracks[j].trace)):
                            x = int(self.tracker.tracks[j].trace[k][0,0])
                            y = int(self.tracker.tracks[j].trace[k][0,1])
                            cv2.circle(frame,(x,y), 2, self.track_colors[j],-2)

                    try:
                        if(len(newData)>1):
                            dataPhiAttribute.append( self.attribut.phi( x1=newData[len(newData)-1][0], 
                                                                   x0=newData[len(newData)-2][0],
                                                                   y1=newData[len(newData)-1][1],
                                                                   y0=newData[len(newData)-2][1]))
                            
                    except:
                        error=1
                        
                #print(len(newData))

                try:
                    cv2.imshow('image',frame)
                except:
                    print("\n-------- Data Collected---------\n")  
                    #print("nbr =  {} ".format(self.insects.getNumberOfFrames()) )
                    return dataPhiAttribute
                    
                i=i+1
                
            #Sleep time between frames
                #*********time.sleep(0.1)
                
                ##########################################
                #
                #     Press 'q' button to quit track
                #
                ##########################################
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("\n-------- Quit Track ---------\n")
                    cv2.destroyAllWindows()
                    break
    


    def getGlobalClass(self):
 
        return self.globl               
            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
