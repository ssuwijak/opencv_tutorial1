import os
import cv2 as cv
import numpy as np

# contour .. used for shape analysis, oject detection and recognition
# edge
def read_img(img_path):
    img = cv.imread(img_path)
    cv.imshow('Image', img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)





if __name__ == '__main__':
    path_main = r"..\..\opencv-course-master\Resources"
    read_img(os.path.join(path_main, 'Photos', 'cat.jpg'))

    cv.waitKey(0)
    cv.destroyAllWindows()

    print("done")
