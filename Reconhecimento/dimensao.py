from pydonesia import ComputerVision
import os

def dimensoes():

    cv = ComputerVision()

    cwd = os.getcwd()

    file_all = os.listdir(cwd)

    images = []
    for f in file_all:
        if f.lower().endswith('jpg'): images.append(f)

    for i in images:
        image = i
        cv.measure_object_dimension(image, coin_diameter = 3.8, unit = 'cm')