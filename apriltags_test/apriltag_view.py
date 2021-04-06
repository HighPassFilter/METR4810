# Detect Apriltag fiducials in Raspbery Pi camera image
# From iosoft.blog
 
import cv2
import apriltag
import time
import stat
import os

TITLE      = "apriltag_view"  # Window title
TAG        = "tag16h5"        # Tag family
MIN_MARGIN = 10               # Filter value for tag detection
FONT       = cv2.FONT_HERSHEY_SIMPLEX  # Font for ID value
RED        = 0,0,255          # Colour of ident & frame (BGR)
TAG_IDs    = [2,3,0]                # Tag we are looking for
 
if __name__ == '__main__':


    cam = cv2.VideoCapture(2)
    detector = apriltag.Detector(apriltag.DetectorOptions(families=TAG))
    

    while cv2.waitKey(1) != 0x1b:
        
        ret, img = cam.read()
        greys = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dets = detector.detect(greys)

        if len(dets) > 0:
            for det in dets:
                if (det.decision_margin >= MIN_MARGIN) & (det.tag_id in TAG_IDs):
                    rect = det.corners.astype(int).reshape((-1,1,2))
                    cv2.polylines(img, [rect], True, RED, 2)
                    ident = str(det.tag_id)
                    pos = det.center.astype(int) + (-10,10)
                    cv2.putText(img, ident, tuple(pos), FONT, 1, RED, 2)
                    print(chr(27) + "[2J")
                    print(det.tag_id,det.corners)

        cv2.imshow(TITLE, img)

        #time.sleep(1/5)


    cv2.destroyAllWindows()
