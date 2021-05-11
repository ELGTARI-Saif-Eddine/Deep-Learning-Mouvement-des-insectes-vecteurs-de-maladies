from InsectsTrack import InsectsTrack 
from Classifier import SvmClassifier



def main():
    classifier= SvmClassifier(path='C:\\Users\\Saif\\Desktop\\phlebotome_videos\\',file_name='data_base.csv')

    insectsTrack = InsectsTrack()
    insectsTrack.track(classifier=classifier)

        
        
    ###############################################################################################################
    #  Note:
    #      timeToStartCapture=5
    # 
    # set a specific starting frame number, to start detecting insects correctly (Example timeToStartCapture=5)   
    # timeToStartCapture is the frame number once insects start moving
    # 
    ###############################################################################################################           
    
    
                ##########################################
                #
                #     Press 'q' button to quit track
                #
                ##########################################    
        
       

if __name__ == '__main__':
    main()
    