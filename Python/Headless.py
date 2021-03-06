import time
import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont # all of the librarys

lsm303 = Adafruit_LSM303.LSM303()
RST = 24
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) # lets the display actullay work and communicate

disp.begin()
disp.clear()
disp.display() # clears and starts up the display

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
padding = 2
shape_width = 20
top = padding
bottom = height-padding
x = padding # all the math required to draw the preety pictures we want


while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    print('Accel X={0}, Accel Y={1}, Mag X={3}, Mag Y={4}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
    # Wait half a second and repeat.
    time.sleep(0.5)
    
    accel_x = (round(accel_x/101.936, 0) * 3)+32 # gets all the values into ms^2 then makes sure they are the right format
    accel_y = (round(accel_y/101.936, 0) * 5)+64
    
    draw.ellipse((accel_y-5, accel_x-5, accel_y+5, accel_x+5), outline=255) # draws the circle that represents the "buble" in our level
    
    draw.line((64, bottom, 64, top), fill=255) 
    draw.line((0, 32, 128, 32), fill=255) # draws a centerline on the verticle and horizontal axis
    
    disp.image(image)
    disp.display() # makes sure everything actually shows up.
    
    draw.rectangle((0,0,width,height), outline=0, fill=0)raspstill - k # wipes the screen
