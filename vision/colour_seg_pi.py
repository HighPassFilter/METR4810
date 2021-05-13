from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np

camera = PiCamera()
rawCapture = PiRGBArray(camera)
time.sleep(0.1)

def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_center_target():


    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    rawCapture.truncate(0)

    lower = np.array([0,100,50], dtype = "uint8")
    upper = np.array([30,255,255], dtype = "uint8")

    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    curr_mask = cv2.inRange(hsv_img, lower, upper)
    hsv_img[curr_mask > 0] = ([15,255,200])
    hsv_img[curr_mask == 0] = ([0,0,0])

    output = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
    gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)

    ret, threshold = cv2.threshold(gray, 90, 255, 0)

    contours, hierarchy =  cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

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
            cv2.circle(image, (cX, cY), 7, (0, 0, 255), -1)
            return (cx, cy)
        except:
            pass
    return (-1,-1)

while (True):
    print(get_center_target)