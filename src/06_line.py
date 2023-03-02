import cv2 as cv
import numpy as np


def lines():
    canvas = np.zeros((500, 500, 3), dtype='uint8')
    # cv.imshow('Black', canvas)
    width = canvas.shape[1]
    height = canvas.shape[0]

    width_mid = width//2
    height_mid = height//2

    cv.line(canvas, (200, 0), (width_mid, height_mid), (0, 255, 0), thickness=2)
    cv.line(canvas, (0, 0), (50, 100), (255, 0, 0), thickness=2)

    cv.imshow('Lines', canvas)


if __name__ == '__main__':
    lines()
    cv.waitKey(0)
    cv.destroyAllWindows()
