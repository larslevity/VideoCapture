"""

https://picamera.readthedocs.io/en/release-1.10/recipes1.html

"""


import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_recording('my_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()