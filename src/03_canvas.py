import cv2 as cv
import numpy as np


def create_canvas1():
    # init. a 500x500 canvas pixel with black (zeroes) color
    canvas = np.zeros((500, 500, 3), dtype='uint8')
    cv.imshow('Blank', canvas)


def create_canvas2():
    # init. a 500x500 canvas pixels with 3 color channels (R,G,B)
    canvas = np.zeros((500, 500, 3), np.uint8)
    cv.imshow('Black', canvas)

    canvas[:] = 0, 255, 0  # change color black (zeroes) to green color
    cv.imshow('Green', canvas)

    canvas[:] = 0, 0, 255
    cv.imshow('Red', canvas)

    canvas[200:300, 300:400] = 255, 0, 0
    cv.imshow('Partial Blue', canvas)


if __name__ == '__main__':
    # create_canvas1()
    create_canvas2()
    cv.waitKey(0)
    cv.destroyAllWindows()
