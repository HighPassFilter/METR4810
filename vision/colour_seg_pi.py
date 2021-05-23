import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
from threading import Thread
from queue import Queue

class Vision:
    def __init__(self, framerate=30):
        # initialize the camera
        self.camera = PiCamera()

        # set camera parameters
        self.camera.resolution = (1280, 720)
        self.camera.framerate = framerate

        # initialize the stream
        self.rawCapture = PiRGBArray(self.camera, self.camera.resolution)
        self.stream = self.camera.capture_continuous(self.rawCapture, 
            format="bgr", use_video_port=True)

        # initialize the frame and the variable used to indicate
        # if the thread should be stopped
        self.frame = None
        self.stopped = False

        self.measure = MeasureTime()

    def start(self):
        # start the thread to read frames from the video stream
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        for f in self.stream:
            # grab the frame from the stream and clear the stream in
            # preparation for the next frame
            self.frame = f.array
            self.rawCapture.truncate(0)
            #print("hi")

            # if the thread indicator variable is set, stop the thread
            # and resource camera resources
            if self.stopped:
                self.stream.close()
                self.rawCapture.close()
                self.camera.close()
                return

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

    def get_center_target(self):
        # Get image from the camera
        image = self.frame

        # Set HSV colour filter bounds of interest 
        lower = np.array([0,150,100], dtype = "uint8")
        upper = np.array([15,255,255], dtype = "uint8")

        # Convert the RGB image to HSV
        hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Filter the pixels that are not within the colour range
        curr_mask = cv2.inRange(hsv_img, lower, upper)

        # Find the contours of the valid pixels
        contours, hierarchy =  cv2.findContours(curr_mask ,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        # Find the centre of the largest orange object in the camera view
        largestCont = None
        largestArea = -1
        for cont in contours:
            # Obtain the area of each individual closed contour area
            area = cv2.contourArea(cont)
            if area > largestArea:
                largestArea = area
                largestCont = cont
        if len(contours) > 0:
            # Obtain the centre of each individual
            M = cv2.moments(largestCont)
            try:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                # Return the centre of the largest orange pixels
                return (cX - image.shape[1]/2, cY - image.shape[0]/2, largestArea)
            except:
                pass
        
        # Return 0 if no closed contours of orange pixels are detected 
        return (0,0,0)     

class MeasureTime():
    def tic(self):
        self.start = time.time()

    def toc(self):
        duration = time.time() - self.start
        print(duration)


def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    vision = Vision()
    vision.start()
    time.sleep(2)
    start = time.time()
    while True:
        image = vision.read()
        start = time.time()
        centre = vision.get_center_target()
        print(centre)
        duration = time.time() - start
        print('Total time:')
        print(duration)
        image = cv2.circle(image, (int(centre[0]), int(centre[1])), 7, (0, 0, 255), -1)
        cv2.imshow('image', image)
        cv2.waitKey(1)

    cv2.destroyAllWindows()