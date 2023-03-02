import os
import cv2 as cv


def read_vid(vid_path):
    capture = cv.VideoCapture(vid_path)
    # capture = cv.VideoCapture(0) # camera or webcam 0
    # capture = cv.VideoCapture(1) # camera or webcam 1
    # capture = cv.VideoCapture(2) # camera or webcam 2
    # capture.isOpened() <-- check camera is ready or not

    isTrue = True

    while isTrue:
        isTrue, frame = capture.read()
        if isTrue:
            frame_resized = resizeFrame(frame, .5)

            cv.imshow('Video', frame)
            cv.imshow('Video Resized', frame_resized)

            # cv.waitKey(value) : max value = slow, min value = fast, default = 20~25
            if cv.waitKey(1) & 0xFF == ord('d'):
                break

    capture.release()
    cv.destroyAllWindows()


def resizeFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]*scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    capture = cv.VideoCapture(0)
    capture.set(4, width)
    capture.set(3, height)


if __name__ == '__main__':
    path_main = r"..\..\opencv-course-master\Resources"
    # print(ord('d'),hex(100))
    read_vid(os.path.join(path_main, 'Videos', 'dog.mp4'))
    print("done")
