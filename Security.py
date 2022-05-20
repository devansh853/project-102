from tkinter import Frame
from unittest import result
import cv2
def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,Frame = videoCaptureObject.read()
        cv2.imwrite('newpicture1.jpg',Frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
take_snapshot()
