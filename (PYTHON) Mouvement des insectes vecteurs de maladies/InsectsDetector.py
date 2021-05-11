import numpy
import cv2
from Filters import Filters
from warnings import catch_warnings


class InsectsSubtractor(object):
    
    def __init__(self,globl):
        super(InsectSubtractor, self).__init__()
        self.globl = globl
        '''Get video source GOPR0011_2.avi // GOPR0729_2.avi //  GOPR0776_2.avi  //GOPR0011_2.avi   //0660.MP4'''
        self.cap = cv2.VideoCapture(self.globl.path())
        '''Get number of frames from loaded video'''
        self.frames_num =int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        '''Background subtraction Instance From OpenCV library '''
        #self.fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = False)
        self.fgbg = cv2.createBackgroundSubtractorMOG2(history=5, varThreshold=50, detectShadows=False)
        ''' Filtres and Contracts adjustments '''
        self.alpha = 1.5 # Contrast control (1.0-3.0)
        self.beta = 0 # Brightness control (0-100)
        '''Start Tracking'''
        self.kernel1 = numpy.ones((5, 5), numpy.uint8)
        self.kernel2 = numpy.ones((1, 1), numpy.uint8)
        self.filter= Filters(3)
        
        self.saveValue=0
        self.saveValue2=0
        
        # measuredTrack =numpy.zeros((self.getNumberOfFrames(),2))-1


    def __del__(self): 
        del self.filter
 
 
    

    def startTracking(self,i):

        while(i<self.frames_num):
                frame = self.cap.read()[1]
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                #frame = cv2.threshold(frame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                #-------------frame = cv2.convertScaleAbs(frame, alpha=self.alpha, beta=self.beta)
    
                fgmask = self.fgbg.apply(frame)
                fgmask=self.filter.filterApply(fgmask) 

                '''get object position '''
                #---------ret,thresh = cv2.threshold(fgmask,127,255,0)
                ret,thresh = cv2.threshold(fgmask,127,255,cv2.THRESH_BINARY)

                contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
                if len(contours) > 0:
                    cv2.imshow('fgmask',fgmask)
                    #return contours
                k = cv2.waitKey(1) & 0xff
                i=i+1       
            

    def getInsectsCoordinates(self):
        
        frame = self.cap.read()[1]
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        fgmask = self.fgbg.apply(frame)
            
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame = cv2.threshold(frame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #--------------frame = cv2.convertScaleAbs(frame, alpha=self.alpha, beta=self.beta)
        #--------------fgmask = self.fgbg.apply(frame)
        
        try:
            fgmask=self.filter.filterApply(fgmask) 
        except: 
            #print('ERROR 4')
            err=1 
        ret,thresh = cv2.threshold(fgmask,127,255,0,cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContour(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        '''get object position '''
        #------ret,thresh = cv2.threshold(fgmask,127,255,0)
        #------contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
            
        measuredTrack = [[0,0]]
               
        if (len(contours) > 0):
            #measuredTrack = [[0, 0]]

            
            try:
                self.saveValue=numpy.mean(contour[0],axis=0).astype(int)
                
                #self.saveValue2 =        
                #measuredTrack.append(numpy.mean(contours[u],axis=0).astype(int)[0])
                measuredTrack=[numpy.mean(contours[u],axis=0).astype(int)[0]
                               for u in range(0, len(contours))]
                
            except: 
                print("ERROR 1")
                t=2  
        
        Tab=numpy.array(measuredTrack)
       
        return Tab
         
          
    def getActualFrame(self):
        
        
        frame = self.cap.read()[1]
    
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame = cv2.threshold(frame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #-----frame = cv2.convertScaleAbs(frame, alpha=self.alpha, beta=self.beta)
        fgmask = self.fgbg.apply(frame)
        

        
        try:
            fgmask=self.filter.filterApply(fgmask) 
        except: 
            #print('ERROR 3')
            error=1 
        #return frame 
        return fgmask
    
    def getActualRealFrame(self):
        
        
        frame = self.cap.read()[1]
    
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame = cv2.threshold(frame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #-----frame = cv2.convertScaleAbs(frame, alpha=self.alpha, beta=self.beta)
        
        '''
        fgmask = self.fgbg.apply(frame)
        try:
            fgmask=self.filter.filterApply(fgmask) 
        except: 
            #print('ERROR 3')
            error=1 
        #return frame 
        return fgmask   
        '''
        
        return frame   
            
    def getNumberOfFrames(self):
        
        return self.frames_num       
    
    def getGlobalClass(self):
        
        return self.globl    
       
    def initialization(self):
        self.cap = cv2.VideoCapture(self.globl.path())
            
            
        
