
class Global(object):
    
    def __init__(self):
        super(Global, self).__init__()
        self.videoPath = 'C:\\Users\\Saif\\Desktop\\phlebotome_videos\\DB\\Phleb\\'
        
        '''Get video source GOPR0011_2.avi // GOPR0729_2.avi //  GOPR0776_2.avi  //GOPR0011_2.avi   //0660.MP4  //bugs0_5.mp4 '''
        self.videoFile = '1.avi'

    def path(self):       
        self.video = self.videoPath +self.videoFile
        return self.video
    
    def setVideoName(self,video_path , video_name):
        self.videoPath= video_path
        self.videoFile=video_name