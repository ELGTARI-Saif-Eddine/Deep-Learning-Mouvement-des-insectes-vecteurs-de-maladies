from Train import Train 


def main():
    
    train=Train(path='C:\\Users\\Saif\\Desktop\\phlebotome_videos\\DB\\Phleb\\',  video_list=['1.avi','2.avi',
                                          '4.avi','5.avi','7.avi','8.avi','9.avi','10.avi','11.avi','12.avi','13.avi'
                                         ,'14.avi','15.avi','16.avi','18.avi','19.avi','20.avi','21.avi','22.avi','23.avi','24.avi','25.avi'])
    train.startCollectingData()
    
    #######################################################################
    #  Note:
    #     path='...' :set your location of Videos Folder
    #     video_list=['...','...','...','...']  :set your videos list
    #
    #######################################################################
                ##########################################
                #
                #     Press 'q' button to quit track
                #
                ##########################################    
        
       
if __name__ == '__main__':
    main()
   