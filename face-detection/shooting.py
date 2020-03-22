import pypylon.pylon as py
import cv2


def shoot():
    device = py.TlFactory.GetInstance().CreateFirstDevice()
    camera = py.InstantCamera(device)
    
    camera.Open()

    camera.StartGrabbing(py.GrabStrategy_LatestImages)
    
    while True:
        if camera.NumReadyBuffers:
            image = camera.RetrieveResult(1000)
            if image:
                try:
                    if image.GrabSucceeded(): 
                        grab_image = image.Array
                finally:
                    image.Release()
        cv2.imshow("Shooting", grab_image)
        cv2.waitKey(1)

shoot()
