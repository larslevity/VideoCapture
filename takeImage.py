
import picamera

class Camera(object):
    def __init__(self, resolution=(1024, 1024)):
        self.camera = picamera.PiCamera()
        self.camera.resolution = resolution
        self.camera.start_preview()

    def save_img(self, filename):
	self.camera.capture(filename)


cam = Camera()

filename = 'image.jpg'

cam.save_img(filename)
