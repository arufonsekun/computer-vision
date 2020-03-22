import pypylon.pylon as py
import cv2

"""
    This sample code take a single shoot using Basler ace acA1300-200um
"""

def plot(msg, image):

    cv2.imshow(msg, image)
    cv2.waitKey()

def grabImage():

    device = py.TlFactory.GetInstance().CreateFirstDevice()
    camera = py.InstantCamera(device)
    camera.Open()

    # Grab a single  camera image
    grab_image = camera.GrabOne(400)
    image = grab_image.Array

    return image

image = grabImage();
plot("Teste", image)
    
