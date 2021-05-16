import cv2
import numpy as np

def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



cap = cv2.VideoCapture(0)

#while True:
if True:
    ret, frame = cap.read()
    #image = frame
    image = cv2.imread("vision/unknown.png")
    viewImage(image)
    # create NumPy arrays from the boundaries
    # blue is 110 to 130
    # for the red
    lower = np.array([0,150,100], dtype = "uint8")
    upper = np.array([15,255,255], dtype = "uint8")
    # for the blue
    # lower = np.array([110,100,50], dtype = "uint8")
    # upper = np.array([130,255,200], dtype = "uint8")
    # find the colors within the specified boundaries and apply
    # the mask
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #print(hsv_img[2000][1500])
    viewImage(hsv_img) ## 2

    curr_mask = cv2.inRange(hsv_img, lower, upper)
    hsv_img[curr_mask > 0] = ([15,255,200])
    hsv_img[curr_mask == 0] = ([0,0,0])


    # mask = cv2.inRange(image, lower, upper)
    # output = cv2.bitwise_and(image, image, mask = mask)
    viewImage(hsv_img) ## 2

    output = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
    gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
    viewImage(gray) ## 3

    ret, threshold = cv2.threshold(gray, 90, 255, 0)
    viewImage(threshold) ## 4

    contours, hierarchy =  cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
    viewImage(image) ## 5

    largestCont = None
    largestArea = -1
    for cont in contours:
        area = cv2.contourArea(cont)
        if area > largestArea:
            largestArea = area
            largestCont = cont
    if len(contours) > 0:
        cv2.drawContours(image, [largestCont], 0, (255, 255, 255), 3)
        M = cv2.moments(largestCont)
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            print(cX, cY)
            cv2.circle(image, (cX, cY), 20, (255, 255, 255), -1)
        except:
            pass
    # imS = cv2.resize(image, (960, 900)) 
    # cv2.imshow('frame', imS)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     pass
    viewImage(image) ## 5