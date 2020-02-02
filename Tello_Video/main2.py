#!/usr/bin/python3
import tello
import tellovideo
import cv2

def main():
    
    drone = tello.Tello('', 8889)
    # for testting using a camera use tellovideo.TelloVideo(0)
    droneStream = tellovideo.TelloVideo("udp://@0.0.0.0:11111")
    
    
    while True:
        try:
            droneStream.show_frame(1)  
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
