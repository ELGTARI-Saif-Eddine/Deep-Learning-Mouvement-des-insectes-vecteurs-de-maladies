import numpy
import cv2


class Filters(object):
    
    def __init__(self,kernelSize):
        
        super(Filters, self).__init__()
        self.kernel1 = numpy.ones((3,3), numpy.uint8)
        
        
        self.kernel2 = numpy.ones((1, 1), numpy.uint8)
        self.kernel3 = numpy.ones((1, 1), numpy.uint8)

      
 
    def openMorphology(self,img): 
      
        #---newImg = cv2.split(img)[0]
        #retVal, newImg) = cv2.threshold(newImg, 130, 255, cv2.THRESH_BINARY)
        #newImg = cv2.morphologyEx(newImg, cv2.MORPH_OPEN, self.kernel)
        newImg = cv2.morphologyEx(image, cv2.MORPH_OPEN, numpy.ones((3,3), numpy.uint8))   # ERROR
        newImg = cv2.dilate(newImg,numpy.ones((3,3), numpy.uint8),iterations = 4)

      
        return newImg
    

    def filterApply(self,img):
         
                 
        #try:
        #    fgmask=self.filter.filterApply(img) 
        #except: 
        #    print('ERROR 5')
            
        #fgmask=self.filter.filterApply(img) 

        ''' filtering noise from foreground mask   '''
        fgmask = self.openMorphologyAply(img)  
        return fgmask
    
    
    
    def startTrackingv3():
    
        kernel = numpy.ones((5,5), numpy.uint8)
        ''' Filtres and Contracts adjustments '''
        alpha = 2.6 # Contrast control (1.0-3.0)
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
            #mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            res =  cv2.bitwised_and(frame, frame, mask= mask)
            mask = cv2.dilate(mask,numpy.ones((3,3), numpy.uint8),iterations = 4)
            #mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, numpy.ones((4,4), numpy.uint8))


            contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            if(len(contours)>0):
                s=s+1
                #print(len(contours))
                #print('***') 
                #print(s)
        
            print(len(contour))    
            cv2.imshow("Frame", res)
            cv2.imshow("mask", mask)
            key = cv2.waitKey(30)
            if key == 27:
                break
            
        cap.release()
        cv2.destroyAllWindows()


        
           
