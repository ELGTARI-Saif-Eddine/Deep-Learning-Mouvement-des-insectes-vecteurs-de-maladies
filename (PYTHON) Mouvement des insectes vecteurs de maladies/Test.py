#Import pandas package as pd
import pandas as pd
import cv2
import numpy




#insects=InsectsSubtractor()

#insects.startTracking(i=0)

#i=0
#while(i<insects.getNumberOfFrames()):
#    contrs=insects.getInsectsCoordinates()
#    print(contrs) 
#    i=i+1




def startTracking():
    
            
    '''Get video source GOPR0011_2.avi // GOPR0729_2.avi //  GOPR0776_2.avi  //GOPR0011_2.avi   //0660.MP4'''
    cap = cv2.VideoCapture('C:\\Users\\Saif\\Desktop\\phlebotome_videos\\DB\\Phleb\\1.avi')
    
    '''Get number of frames from loaded video'''
    frames_num =int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    '''Background subtraction Instance From OpenCV library '''
    fgbg = cv2.createBackgroundSubtractorKNN(detectShadows = False)
        
    ''' Filtres and Contracts adjustments '''
    alpha = 1.6 # Contrast control (1.0-3.0)
    beta = 0 # Brightness control (0-100)
    '''Start Tracking'''
    
    kernel = numpy.ones((3,3), numpy.uint8)
    kernel1 = numpy.ones((1, 1), numpy.uint8)
    kernel2 = numpy.ones((1, 1), numpy.uint8)
        
    saveValue=0
    saveValue2=0        

    
    i=0    
    while(i<frames_num):
        frame = cap.read()[1]
    
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame = cv2.threshold(frame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
        fgmask = fgbg.apply(frame)
        
        
        
        #fgmask=cv2.GaussianBlur(fgmask,(5, 5), 0)

        #/////fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel1, iterations=5)
                 #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel2, iterations=4)
        #/////fgmask = cv2.split(fgmask)[0]
        #/////(retVal, fgmask) = cv2.threshold(fgmask, 130, 255, cv2.THRESH_BINARY)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        
        #/////fgmask=cv2.medianBlur(fgmask,3)
        
        

        
        


        '''get object position '''
        ret,thresh = cv2.threshold(fgmask,127,255,cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        #////////print(len(contours))
        
        if len(contours) >= 0:
            cv2.imshow('fgmask',fgmask)
            print(len(contours))
            #return contours
            k = cv2.waitKey(1) & 0xff
            i=i+1       



def startTrackingv2():
    
            
    '''Get video source GOPR0011_2.avi // GOPR0729_2.avi //  GOPR0776_2.avi  //GOPR0011_2.avi   //0660.MP4'''
    cap = cv2.VideoCapture('C:\\Users\\Saif\\Desktop\\phlebotome_videos\\DB\\Phleb\\1.avi')
    _, first_frame = cap.read()
    first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)
    
    while True:
        _, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
        difference = cv2.absdiff(first_gray, gray_frame)
        _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(difference,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        print(len(contours)) 
        cv2.imshow("First frame", first_frame)
        cv2.imshow("Frame", frame)
        cv2.imshow("difference", difference)
   
        key = cv2.waitKey(30)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def startTrackingv3():
    
    kernel = numpy.ones((5,5), numpy.uint8)
    ''' Filtres and Contracts adjustments '''
    alpha = 1.6 # Contrast control (1.0-3.0)
    beta = 0 # Brightness control (0-100)

    '''Get video source GOPR0011_2.avi // GOPR0729_2.avi //  GOPR0776_2.avi  //GOPR0011_2.avi   //0660.MP4'''
    cap = cv2.VideoCapture('C:\\Users\\Saif\\Desktop\\phlebotome_videos\\DB\\Phleb\\1.avi')
    frames_num =int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    subtractor = cv2.createBackgroundSubtractorMOG2(history=5, varThreshold=50, detectShadows=False)
    s=0
    i=0
    while (i<frames_num):
        
        i=i+1

        _, frame = cap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

        mask = subtractor.apply(frame)
        #mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, numpy.ones((3,3), numpy.uint8))
        #mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.dilate(mask,numpy.ones((3,3), numpy.uint8),iterations = 4)
        #mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, numpy.ones((4,4), numpy.uint8))
        #mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, numpy.ones((2,2), numpy.uint8))
        res =  cv2.bitwise_and(frame, frame, mask= mask)
        #mask = cv2.erode(mask, kernel, iterations = 3)

        ret,thresh = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if(len(contours)>0):
            s=s+1
            #print(len(contours))
            #print('***') 
            #print(s)
        
        print(len(contours))    
        cv2.imshow("Frame", res)
        cv2.imshow("mask", mask)
        key = cv2.waitKey(30)
        if key == 27:
            break
            
    cap.release()
    cv2.destroyAllWindows()




def startTrackingv4():
    
    kernel = numpy.ones((5,5), numpy.uint8)
    ''' Filtres and Contracts adjustments '''
    alpha = 1.6 # Contrast control (1.0-3.0)
    beta = 0 # Brightness control (0-100)

    '''Get video source GOPR0011_2.avi // GOPR0729_2.avi //  GOPR0776_2.avi  //GOPR0011_2.avi   //0660.MP4'''
    cap = cv2.VideoCapture('C:\\Users\\Saif\\Desktop\\phlebotome_videos\\DB\\Phleb\\1.avi')
    frames_num =int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    subtractor = cv2.createBackgroundSubtractorMOG2(history=5, varThreshold=50, detectShadows=False)
    s=0
    i=0
    while (i<frames_num):
        
        i=i+1

        _, frame = cap.read() 
        frame = cv2.split(frame)
       
            
        cv2.imshow("Frame", frame) 
        
        
        key = cv2.waitKey(30)
        if key == 27:
            break
            
            
    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    startTrackingv3()
    
    