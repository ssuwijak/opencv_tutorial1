import os
import cv2 as cv


def read_img(img_path):
    img = cv.imread(img_path)
    cv.imshow('Image', img)

    # convert to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    # Blur
    # kernel size = a tuple enables more or less blur by an odd numbers --> 3,5,7,9,11,...
    ksize = 5
    blur = cv.GaussianBlur(img, (ksize, ksize), cv.BORDER_DEFAULT)
    cv.imshow('Blur', blur)

    # Edge Cascade
    threshold_list = [125, 175]  # threshold min and max
    canny = cv.Canny(blur, threshold_list[0], threshold_list[1])
    cv.imshow('Canny Edge', canny)

    # Dilating the image .. pronouce as dai-late
    dilated = cv.dilate(canny, (7, 7), iterations=3)
    cv.imshow('Dilated', dilated)

    # Eroding
    eroded = cv.erode(dilated, (3, 3), iterations=1)
    cv.imshow('Erode', eroded)

    # Resize
    resized = cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
    cv.imshow('Resized',resized)

    # Cropping
    cropped = img[50:200,200:400]
    cv.imshow('Cropped', cropped)


if __name__ == '__main__':
    path_main = r"..\..\opencv-course-master\Resources"
    read_img(os.path.join(path_main, 'Photos', 'cat.jpg'))

    cv.waitKey(0)
    cv.destroyAllWindows()

    print("done")
