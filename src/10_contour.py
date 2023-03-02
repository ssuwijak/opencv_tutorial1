import os
import cv2 as cv
import numpy as np

'''
contour .. used for shape analysis, oject detection and recognition
- For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
- Since OpenCV 3.2, findContours() no longer modifies the source image but returns a modified image as the first of three return parameters.
- In OpenCV, finding contours is like finding white object from black background. 
    So remember, object to be found should be white and background should be black.
'''


def read_img(img_path):
    img = cv.imread(img_path)
    cv.imshow('Image', img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    canny = cv.Canny(img,125,175)
    cv.imshow('Canny', canny)

    contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
    print(f'found {len(contours)} contour(s)')

    #hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

if __name__ == '__main__':
    path_main = r"..\..\opencv-course-master\Resources"
    read_img(os.path.join(path_main, 'Photos', 'cat.jpg'))

    cv.waitKey(0)
    cv.destroyAllWindows()

    print("done")
