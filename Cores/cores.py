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

    recontB = 0
    recontR = 0
    recontG = 0
    recontY = 0
    recontW = 0
    recontBl = 0
    cor = ''

    # Iterate until the user presses ESC key

    f = open("..\Reconhecimento\Laudo_faca.doc", "a")

    while True:
        frame = get_frame(cap, scaling_factor)

        # Convert the HSV colorspace
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define 'blue' range in HSV colorspace
        lowerB = np.array([110,50,50])
        upperB = np.array([130,255,255])

        # Define 'red' range in HSV colorspace
        lowerR = np.array([0, 70, 50])
        upperR = np.array([10, 255, 255])

        # Define 'yellow' range in HSV colorspace
        lowerY = np.array([20, 100, 100])
        upperY = np.array([30, 255, 255])

        # Define 'green' range in HSV colorspace
        lowerG = np.array([65, 60, 60])
        upperG = np.array([80, 255, 255])

        # Define 'white' range in HSV colorspace
        lowerW = np.array([0, 0, 0])
        upperW = np.array([0, 255, 255])

        # Define 'black' range in HSV colorspace
        lowerBl = np.array([125, 100, 30])
        upperBl = np.array([255, 255, 255])

        # Threshold the HSV image to get only the color
        maskB = cv2.inRange(hsv, lowerB, upperB)
        maskR = cv2.inRange(hsv, lowerR, upperR)
        maskG = cv2.inRange(hsv, lowerG, upperG)
        maskY = cv2.inRange(hsv, lowerY, upperY)
        maskW = cv2.inRange(hsv, lowerW, upperW)
        maskBl = cv2.inRange(hsv, lowerBl, upperBl)

        contB = 0
        contR = 0
        contG = 0
        contY = 0
        contW = 0
        contBl = 0

        for i in range(18):
            for j in range(10):
                if maskB[i][j] == 255:
                    contB = contB + 1
                if maskR[i][j] == 255:
                    contR = contR + 1
                if maskG[i][j] == 255:
                    contG = contG + 1
                if maskY[i][j] == 255:
                    contY = contY + 1
                if maskW[i][j] == 255:
                    contW = contW + 1
                if maskBl[i][j] == 255:
                    contBl = contBl + 1

        if contB > 150:
            print("azul")
            recontB = recontB + 1

        if contR > 150:
            print("vermelho")
            recontR = recontR + 1

        if contG > 150:
            print("verde")
            recontG = recontG + 1

        if contY > 150:
            print("amarelo")
            recontY = recontY + 1

        if contW > 150:
            print("branco")
            recontW = recontW + 1

        if contBl > 150:
            print("preta")
            recontBl = recontBl + 1



        # Bitwise-AND mask and original image
        resB = cv2.bitwise_and(frame, frame, mask=maskB)
        resB = cv2.medianBlur(resB, 5)

        resR = cv2.bitwise_and(frame, frame, mask=maskR)
        resR = cv2.medianBlur(resR, 5)

        resG = cv2.bitwise_and(frame, frame, mask=maskG)
        resG = cv2.medianBlur(resG, 5)

        resY = cv2.bitwise_and(frame, frame, mask=maskY)
        resY = cv2.medianBlur(resY, 5)

        resW = cv2.bitwise_and(frame, frame, mask=maskW)
        resW = cv2.medianBlur(resW, 5)

        resBl = cv2.bitwise_and(frame, frame, mask=maskBl)
        resBl = cv2.medianBlur(resBl, 5)

        cv2.imshow('Original image', frame)


        # Check if the user pressed ESC key
        c = cv2.waitKey(5)
        if c == 27:
            break
    if recontB > 5:
        print("A cor do cabo é azul")
        cor = "azul"

    if recontR > 5:
        print("A cor do cabo é vermelho")
        cor = "vermelho"

    if recontG > 5:
        print("A cor do cabo é verde")
        cor = "verde"

    if recontY > 5:
        print("A cor do cabo é amarelo")
        cor = "amarelo"

    if recontW > 5:
        print("A cor do cabo é branco")
        cor = "branco"

    if recontBl > 5:
        print("A cor do cabo é preto")
        cor = "preto"

    f.write("\nCor do cabo: " + str(cor))

    cv2.destroyAllWindows()