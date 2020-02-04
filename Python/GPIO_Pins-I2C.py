import time
import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont  # all the libratys we wil need inorder for this code to work... its alot i know

lsm303 = Adafruit_LSM303.LSM303()
RST = 24
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()  # makes sure the display is nice and empty to start
disp.clear()
disp.display()

width = disp.width  # makes sure our lines are nice and preety
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
padding = 2
shape_width = 20
top = padding
bottom = height-padding
x = padding


while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
    # Wait half a second and repeat.
    time.sleep(0.5)
    
    accel_z = round(accel_z/101.936, 2) # rounds the z,x, or y values to two digits after its been divided
    accel_x = round(accel_x/101.936, 2)
    accel_y = round(accel_y/101.936, 2)
    
    draw.rectangle((0,0,width,height), outline=0, fill=0)  # wipes the screen befor the values update
      
    draw.text((x, top),    'ACCEL DATA',  font=font, fill=255) # writes the nice values out to the screen

    draw.text((x, top+20), 'Accel X =' + str(accel_x) + 'm/s^2', font=font, fill=255)
    draw.text((x, top+30), 'Accel Y =' + str(accel_y) + 'm/s^2', font=font, fill=255)
    draw.text((x, top+40), 'Accel Z =' + str(accel_z) + 'm/s^2', font=font, fill=255)

    disp.image(image)
    disp.display()
