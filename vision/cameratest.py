from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
import cv2

camera = PiCamera()
camera.framerate = 32
raw = PiRGBArray(camera)
sleep(0.1)
for frame in camera.capture_continuous(raw, format="bgr", use_video_port=True):
    image = frame.array
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    raw.truncate(0)
    if key == ord("q"):
        break




            
            