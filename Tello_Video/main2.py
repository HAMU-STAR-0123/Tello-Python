#!/usr/bin/python3
import tello
from VideoStreamWidget import VideoStreamWidget
import cv2



def main():
    video_stream_widget = VideoStreamWidget("udp://@0.0.0.0:11111")
    drone = tello.Tello('', 8889)
        
    while True:
        try:
            get = video_stream_widget.show_frame()
            cv2.imshow('Tello', get)
            
            key = cv2.waitKey(1)   
            if key == ord('q'):
                cv2.destroyAllWindows()
                exit(1)
            if key == ord('T'):
                    drone.takeoff()
                    
        except AttributeError:
            pass
       

if __name__ == "__main__":
    main()
