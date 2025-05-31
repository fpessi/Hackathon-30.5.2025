from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow
import os


def take_picture():
    # initialize the camera
    # If you have multiple camera connected with
    # current device, assign a value in cam_port
    # variable according to that

    picture = False
    vc = VideoCapture(0)

    if vc.isOpened():  # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        imshow("Preview. Press Space to take a picture. Press Esc to exit", frame)
        rval, frame = vc.read()
        key = waitKey(20)
        if key == 32:  # exit on Space
            picture = True
            break
        elif key == 27:
            break

    destroyWindow("Preview. Press Space to take a picture. Press Esc to exit")

    # reading the input using the camera
    if picture:
        result, image = vc.read()

    # If image will detected without any error,
    # show result
        if result:

            # showing result, it take frame name and image
            # output

            absolute_path = os.path.dirname(__file__)
            relative_path = r"../Case"
            directory = os.path.join(absolute_path, relative_path)
            os.chdir(directory)
            filename = "Picture.jpg"
            imwrite(filename, image)

            # saving image in local storage

            # If keyboard interrupt occurs, destroy image
            # window

        # If captured image is corrupted, moving to else part
        else:
            print("No image detected.")

            waitKey(0)

    vc.release()
