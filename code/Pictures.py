# program to capture single image from webcam in python
from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow, imread
import os

# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
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

