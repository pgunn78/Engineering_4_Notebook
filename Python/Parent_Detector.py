from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep # libarys we will need

pir = MotionSensor(27)
camera = PiCamera() # initializes the camera and the pin its one


while True:
    print ("scanning")
    pir.wait_for_motion()
    print("motion detected")
    camera.start_preview(fullscreen=False,window=(100,200,400,500)) # when motion detected display what camera sees at this size
    camera.start_recording('/home/pi/Videos/intruder.h264')
    pir.wait_for_no_motion()
    print("no motion")
    camera.stop_recording()
    camera.stop_preview() # when no motio detected display nothing
