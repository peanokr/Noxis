import cv2
import imutils
import time


def takePicture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    (grabbed, frame) = cap.read()
    showimg = frame
    cv2.imshow('img1', showimg)  # display the captured image
    cv2.waitKey(1)
    time.sleep(0.3) # Wait 300 miliseconds
    cap.release()
    return image



