

import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (2048, 2048)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(1)
    camera.capture('image.jpg')
