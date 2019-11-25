from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()

frame = 1
camera.start_preview(fullscreen=False,window=(100,200,400,500))
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/Animation/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
    
    
    
#ffpeg