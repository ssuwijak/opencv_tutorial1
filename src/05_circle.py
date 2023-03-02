import cv2 as cv
import numpy as np


def rectans():
    canvas = np.zeros((500, 500, 3), dtype='uint8')
    # cv.imshow('Black', canvas)
    width = canvas.shape[1]
    height = canvas.shape[0]

    width_mid = width//2
    height_mid = height//2

    cv.circle(canvas, (width_mid, height_mid), 100, (0, 255, 0), thickness=2)
    cv.circle(canvas, (100, 150), 50, (0, 0, 255), thickness=-1)

    cv.imshow('Circle', canvas)


if __name__ == '__main__':
    rectans()
    cv.waitKey(0)
    cv.destroyAllWindows()
