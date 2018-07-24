from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = -90

camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
for i in range(20):
    camera.capture("./imgcap_%03d.jpg"%i)
    sleep(0.25)
camera.stop_preview()
