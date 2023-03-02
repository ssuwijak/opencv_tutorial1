import os
import cv2 as cv


def read_img(img_path):
    img = cv.imread(img_path)
    img_resized = resizeFrame(img, .5)

    cv.imshow('Image', img)
    cv.imshow('Image Resized', img_resized)
    cv.waitKey(0)
    cv.destroyAllWindows()


def resizeFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]*scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


if __name__ == '__main__':
    path_main = r"..\..\opencv-course-master\Resources"
    read_img(os.path.join(path_main, 'Photos', 'cat_large.jpg'))
    print("done")
