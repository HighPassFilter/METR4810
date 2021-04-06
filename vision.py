import apriltag
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# Camera Matrix
fx = 4.04 
fy = 3.04
cx = 1640
cy = 1232
K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])

def get_rot_and_trans():
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
    # allow the camera to warmup
    time.sleep(0.1)
    # grab an image from the camera
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("hit1")
    
    detector = apriltag.Detector()
    print("hit2")
    #detection = detector.detect(grey)
    #print(detection)
    #if detection.hamming <= 2:
        # We have found an april tag
        # Compute required information from it
    #    _, rotations, translations, _ = cv2.decomposeHomographyMat(detection.homography, K)

    #    return rotations, translations
    #else:
    #    return None

get_rot_and_trans()
