from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow
import os


def take_picture():
    """Controls devices camera using python-opencv
    """
    
    # initialize the camera
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
        if key == 32:  # take picture and exit with Space
            picture = True
            break
        elif key == 27: # only exit with Esc
            break

    destroyWindow("Preview. Press Space to take a picture. Press Esc to exit")

    if picture:
        result, image = vc.read()

        if result:
            absolute_path = os.path.dirname(__file__)
            relative_path = r"../Case"
            directory = os.path.join(absolute_path, relative_path)
            os.chdir(directory)
            filename = "Picture.jpg"
            imwrite(filename, image)
        else:
            print("No image detected.")

            waitKey(0)

    vc.release()
