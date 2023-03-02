import cv2 as cv
import numpy as np


def texts():
    canvas = np.zeros((500, 500, 3), dtype='uint8')
    # cv.imshow('Black', canvas)
    x_max = canvas.shape[1]
    y_max = canvas.shape[0]

    x_2 = x_max//2
    y_2 = y_max//2

    y1 = 100
    cv.line(canvas, (0, y1), (x_max, y1), (0, 255, 0), thickness=1)
    cv.putText(canvas, 'y = {}'.format(y1) , (50, y1-2), cv.FONT_HERSHEY_TRIPLEX,
               1.0, (255, 255, 0), thickness=2)
    cv.putText(canvas, 'y = {}'.format(y1) , (200, y1-2), cv.FONT_HERSHEY_TRIPLEX,
            1.5, (255, 255, 0), thickness=2)


    cv.imshow('Texts', canvas)


if __name__ == '__main__':
    texts()
    cv.waitKey(0)
    cv.destroyAllWindows()
