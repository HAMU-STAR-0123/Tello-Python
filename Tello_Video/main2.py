#!/usr/bin/python3
import tellov2 as tello
import tellovideo
import cv2

drone = tello.Tello('', 8889)
droneStream = tellovideo.Video("udp://@0.0.0.0:11111")

def main():
     
    # for testting using a camera use tellovideo.TelloVideo(0)
    while True:
        try:
            droneStream.show_frame(3)  
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                cv2.destroyAllWindows()
                exit(1)
            if key == ord('t'):
                    drone.takeoff()
            if key == ord('l'):
                    drone.land()
                  
        except AttributeError:
            pass
       

if __name__ == "__main__":
    main()
