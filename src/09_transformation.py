import os
import cv2 as cv
import numpy as np


def read_img(img_path):
    img = cv.imread(img_path)
    cv.imshow('Image', img)

    translated = translate(img, 100, -100)
    cv.imshow('Translation', translated)

    rotated = rotate(img, 30)
    cv.imshow('Rotated', rotated)

    flipped = flip(img, 1)
    cv.imshow('Filpped', flipped)


def translate(img, x, y):
    # -x --> shift to left, x --> shift to right
    # -y --> shift to up,   y --> shift to down

    # create an Affine marix 2x3
    # implicit style
    # affine_matrix = [[1, 0, x], [0, 1, y]]  # 2x3 matrix
    # transMatrix = np.float32(affine_matrix)

    # explicit style
    affine_matrix = np.matrix('1,0,-9; 0,1,-9')
    affine_matrix[0, 2] = x  # replace -9 in row_1st by x value
    affine_matrix[1, 2] = y  # replace -9 in row_2nd by y value
    transMatrix = affine_matrix.astype(np.float32)

    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatrix, dimensions)


def rotate(img, angle, rotPoint=None, scale=1.0):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)  # center of the image

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale)

    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


def flip(img, flipMode):
    if flipMode == 0:
        flipMode = 0  # flip over the x-axis (horizontal flip)
    elif flipMode == 1:
        flipMode = 1  # flip over the y-axis (vertical flip)
    elif flipMode == -1:
        flipMode = -1  # flip over both x- and y- axis
    else:
        flipMode = 1

    return cv.flip(img, flipCode=flipMode)


def resize():
    pass


def crop():
    pass


if __name__ == '__main__':
    path_main = r"..\..\opencv-course-master\Resources"
    read_img(os.path.join(path_main, 'Photos', 'cat.jpg'))

    cv.waitKey(0)
    cv.destroyAllWindows()

    print("done")
