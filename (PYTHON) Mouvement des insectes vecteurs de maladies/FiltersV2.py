import numpy
import cv2


class Filters(object):
    
    def __init__(self,kernelSize):
        
        super(Filters, self).__init__()
        self.kernel = numpy.ones((kernelSize,kernelSize), numpy.uint8)
        self.kernel1 = numpy.ones((1, 1), numpy.uint8)
        self.kernel2 = numpy.ones((1, 1), numpy.uint8)

      
 
    def openMorphology(self,img): 
      
        newImg = cv2.split(img)[0]
        (retVal, newImg) = cv2.threshold(newImg, 130, 255, cv2.THRESH_BINARY)
        newImg = cv2.morphologyEx(newImg, cv2.MORPH_OPEN, self.kernel)
        return newImg
    

    def filterApply(self,img):
         
      
        #try:
        #    fgmask=self.filter.filterApply(img) 
        #except: 
        print('ERROR 5')
            

        ''' filtering noise from foreground mask   '''
        fgmask = self.openMorphology(img)  
        return fgmask
    
    
    
    