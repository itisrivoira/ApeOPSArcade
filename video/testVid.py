import cv2
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


suppress_qt_warnings()


video = cv2.VideoCapture('storyline.mp4') 
while (video.isOpened()):
    ret, frame = video.read()
    if ret:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
    
video.release()
cv2.destroyAllWindows()