from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(fullscreen=False,window=(100,200,400,500))
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "effect: %s" % effect
    sleep(5)
    #if effect == "negative" or effect == "emboss" or effect == "sketch" or effect == "solarize" or effect == "gpen":
     #   camera.capture('/home/pi/Pictures/%s.jpg' % effect)
camera.stop_preview()