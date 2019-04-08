#https://github.com/howardabrams/opencv-python-xp/blob/master/color-detection.py

import cv2
import numpy as np

# Capture the input frame from webcam
def get_frame(cap, scaling_factor):
    # Capture the frame from video capture object
    ret, frame = cap.read()

    # Resize the input frame
    frame = cv2.resize(frame, None, fx=scaling_factor,
            fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return frame

if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5

    # Iterate until the user presses ESC key
    while True:
        frame = get_frame(cap, scaling_factor)

        # Convert the HSV colorspace
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define 'blue' range in HSV colorspace
        #lower = np.array([110,50,50])
        #upper = np.array([130,255,255])

        # Define 'red' range in HSV colorspace
        #lower = np.array([0, 70, 50])
        #upper = np.array([10, 255, 255])

        # Define 'yellow' range in HSV colorspace
        #lower = np.array([20, 100, 100])
        #upper = np.array([30, 255, 255])

        # Define 'green' range in HSV colorspace
        #lower = np.array([65, 60, 60])
        #upper = np.array([80, 255, 255])

        # Define 'white' range in HSV colorspace
        #lower = np.array([0, 0, 0])
        #upper = np.array([0, 255, 255])

        # Define 'black' range in HSV colorspace
        lower = np.array([0, 0, 0])
        upper = np.array([180, 255, 30])

        # Define 'black' range in HSV colorspace
        #lower = np.array([125, 100, 30])
        #upper = np.array([255, 255, 255])

        # Threshold the HSV image to get only blue color
        mask = cv2.inRange(hsv, lower, upper)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)
        res = cv2.medianBlur(res, 5)

        cv2.imshow('Original image', frame)
        cv2.imshow('Color Detector', res)

        # Check if the user pressed ESC key
        c = cv2.waitKey(5)
        if c == 27:
            break

    cv2.destroyAllWindows()