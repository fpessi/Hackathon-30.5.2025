import cv2
from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow
import os


def take_picture():
    # initialize the camera
    # If you have multiple camera connected with
    # current device, assign a value in cam_port
    # variable according to that

    vc = cv2.VideoCapture(0)

    if vc.isOpened():  # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 32:  # exit on Space
            break

    vc.release()
    cv2.destroyWindow("preview")

    cam_port = 0
    cam = VideoCapture(cam_port)

    # reading the input using the camera
    result, image = cam.read()

    # If image will detected without any error,
    # show result
    if result:

        # showing result, it take frame name and image
        # output

        absolute_path = os.path.dirname(__file__)
        relative_path = r"../Case"
        directory=os.path.join(absolute_path, relative_path)
        os.chdir(directory)
        filename="Picture.jpg"
        imwrite(filename, image)

        # saving image in local storage

        # If keyboard interrupt occurs, destroy image
        # window

    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")

        waitKey(0)
        destroyWindow("Picture.png")
