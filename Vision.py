import cv2
import numpy as np

class Vision():
    def __init__(self):
        self.capture = cv2.VideoCapture('http://192.168.43.43:8080/stream/video.mjpeg')
    
    def get_centre(self):
        ret, frame = self.capture.read()
        lower = np.array([0,100,100], dtype = "uint8")
        upper = np.array([15,255,255], dtype = "uint8")
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        curr_mask = cv2.inRange(hsv_img, lower, upper)

        contours, hierarchy =  cv2.findContours(curr_mask ,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # Could we directly use the mask here?

        largestCont = None
        largestArea = -1
        for cont in contours:
            area = cv2.contourArea(cont)
            if area > largestArea:
                largestArea = area
                largestCont = cont
        if len(contours) > 0:
            cv2.drawContours(frame, [largestCont], 0, [255,255,255])
            M = cv2.moments(largestCont)
            try:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cX, cY), 7, (0, 0, 255), -1)
                return (frame, cX - frame.shape[1]/2, cY - frame.shape[0]/2, largestArea)
                #return (cX, cY)
            except:
                pass

        return (frame, 0, 0, 0)     