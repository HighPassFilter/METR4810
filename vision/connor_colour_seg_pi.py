import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import io
import numpy as np
from threading import Thread
from queue import Queue

class Vision:
    def __init__(self, framerate=24):
        # initialize the camera
        self.camera = PiCamera()

        # set camera parameters
        self.camera.resolution = (1280, 720)
        self.camera.framerate = framerate

        # initialize the stream
        # self.rawCapture = PiRGBArray(self.camera, self.camera.resolution)
        # self.stream = self.camera.capture_continuous(self.rawCapture, 
        #     format="bgr", use_video_port=True)

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
        image = np.empty((1280, 720, 3), dtype=np.uint8)
        self.camera.capture(image, 'bgr')
        self.frame = image

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

    def get_center_target(self):
        # Get image from the camera
        self.update()
        image = self.frame

        lower = np.array([0,150,100], dtype = "uint8")
        upper = np.array([15,255,255], dtype = "uint8")

        # Perform HSV colour filtering
        # print("<------------------------------------------------------>")
        # print("Convert RGB to HSV")
        # self.measure.tic()
        hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # self.measure.toc()

        # print("HSV Colour thresholding")
        # self.measure.tic()
        curr_mask = cv2.inRange(hsv_img, lower, upper)
        # self.measure.toc()

        # print("HSV equalization(?)")
        # self.measure.tic()
        # hsv_img[curr_mask > 0] = ([15,255,200])
        # self.measure.toc()

        # print("HSV colour filtering")
        # self.measure.tic()
        # hsv_img[curr_mask == 0] = ([0,0,0])
        # self.measure.toc()

        # # Convert HSV colour to RGB
        # print("Convert HSV to RGB")
        # self.measure.tic()
        # output = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB) # Could try directly applying a mask on RGB instead?
        # self.measure.toc()

        # # Convert HSV colour to RGB
        # print("Convert RGB to gray")
        # self.measure.tic()
        # gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
        # self.measure.toc()

        # # Binary thresholding
        # print("Threshold the binary colours")
        # ret, threshold = cv2.threshold(gray, 90, 255, 0)

        contours, hierarchy =  cv2.findContours(curr_mask ,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # Could we directly use the mask here?
        
        # if False in (curr_mask == threshold):
        #     print("Nope :/")
        # else:
        #     print("Absolutely!!!")

        largestCont = None
        largestArea = -1
        for cont in contours:
            area = cv2.contourArea(cont)
            if area > largestArea:
                largestArea = area
                largestCont = cont
        if len(contours) > 0:
            M = cv2.moments(largestCont)
            try:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                #cv2.circle(image, (cX, cY), 7, (0, 0, 255), -1)
                return (cX - image.shape[0]/2, cY - image.shape[1]/2)
                # return (cX, cY)
            except:
                pass
        return (-1,-1)     

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
    time.sleep(2)
    while True:
        t = time.time()
        centre = vision.get_center_target()
        print(centre)
        print(time.time() - t)
    cv2.destroyAllWindows()