# Phython 3.7 
from threading import Thread
import time
#import numpy as np
import cv2

class Video:
    """Wrapper class to read and visualize
       Tello drone video stream.
    """
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(.001)

    def show_frame(self,scale=1):
        height , width , layers = self.frame.shape
        new_h=int(height/scale)
        new_w=int(width/scale)
        if new_h > 0 :
            resize = cv2.resize(self.frame, (new_w, new_h))
        # Display the resulting frame
            cv2.imshow('Tello', resize)
         
        #return resize

