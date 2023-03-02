import cv2 as cv
import numpy as np


def rectan():
    canvas = np.zeros((500, 500, 3), dtype='uint8')
    # cv.imshow('Black', canvas)
    width = canvas.shape[1]
    height = canvas.shape[0]

    cv.rectangle(canvas, (0, 0), (250, 250), (0, 255, 0), thickness=2)

    cv.rectangle(canvas, (250, 250), (300, 350),
                 (255, 0, 0), thickness=cv.FILLED)

    cv.rectangle(canvas, (400, 400), (450, 450), (0, 0, 255), thickness=-1)

    cv.rectangle(canvas, (width//2, height//2),
                 (width//2-50, height//2+50), (127, 127, 0), thickness=1)

    cv.imshow('Rectan', canvas)


if __name__ == '__main__':
    rectan()
    cv.waitKey(0)
    cv.destroyAllWindows()
