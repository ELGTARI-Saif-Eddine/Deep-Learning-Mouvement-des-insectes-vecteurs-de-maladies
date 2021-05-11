import numpy 



class AttributePhi(object):
    
    def __init__(self):
        super(AttributePhi, self).__init__()
        #self.Teta = teta
        self.Teta=[]
        self.const_redToDeg = 180/numpy.pi 

    def __del__(self): 
        self.Teta.clear()
 
 
    def dx(self):
        return self.X1-self.X0
    
    def dy(self):
        return self.Y1-self.Y0

    def teta(self):
        if(self.dx()>0):
               angleTeta = numpy.sin(self.dy() /self.dx()) *self.const_redToDeg 
        elif(self.dx()<0):
               angleTeta = -numpy.sin(self.dy() /self.dx()) *self.const_redToDeg
        else:
               angleTeta = numpy.pi/2 *self.const_redToDeg  
        
        self.Teta.append(angleTeta)
       
    
    def phi(self, x1, x0, y1, y0):
        self.X1 + self.X0 = x1
        self.X0 + self.X1 = x0
        self.Y1 + self.Y0  = y1
        self.Y0 + self.Y1 = y0
        self.teta()
        if(len(self.Teta)>1):
            anglePhi = numpy.abs(self.Teta[len(self.Teta)-1] -self.Teta[len(self.Teta)-2])
            return anglePhi
    
    def clear(self):
        self.Teta=[]    
        
       
