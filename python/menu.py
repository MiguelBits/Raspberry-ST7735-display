# -*- coding:utf-8 -*-
import LCD_1in44 
import LCD_Config 
import RPi.GPIO as GPIO 
import time 
from PIL import Image,ImageDraw,ImageFont,ImageColor 
KEY_UP_PIN = 6 
KEY_DOWN_PIN = 19
KEY_LEFT_PIN = 5 
KEY_RIGHT_PIN = 26 
KEY_PRESS_PIN = 13 
KEY1_PIN = 21 
KEY2_PIN = 20 
KEY3_PIN = 16
#init GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.cleanup() 
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up

# 240x240 display with hardware SPI:
disp = LCD_1in44.LCD() 
Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT #SCAN_DIR_DFT = D2U_L2R 
disp.LCD_Init(Lcd_ScanDir) 
disp.LCD_Clear()
# Create blank image for drawing. Make sure to create image with mode '1' for 1-bit color.
width = 128; height = 128; image = Image.new('RGB', (width, height));
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Draw a black filled box to clear the image.
<<<<<<< HEAD
draw.rectangle((0,0,width,height), outline=0, fill=0) 
draw.text((15, 10), 'Video Games', fill = "GREEN") 
draw.text((15, 20), 'Apps & tools', fill = "GREEN") 
disp.LCD_ShowImage(image,0,0) 
i = 0 
c = 0

while 1:
	draw.text((50, 50), str(c), fill = "GREEN")

	if GPIO.input(KEY_RIGHT_PIN) == 0:
                c += 11

	if i <= 0 : 
		i = 1 
	if i > 2 : 
		i = 2 
	if GPIO.input(KEY_UP_PIN) == 0: 
		i -= 1 
	if GPIO.input(KEY_DOWN_PIN) == 0:
		i += 1 
	if i == 1: # button is released 
		draw.text((15, 10), 'Video Games', fill = "GREEN") 
	else: 
		draw.text((15, 10), 'Video Games', fill = "BLUE")
	if i == 2: 
		draw.text((15, 20), 'Apps & tools', fill = "GREEN")  
	else: 
		draw.text((15, 20), 'Apps & tools', fill = "BLUE") 
	disp.LCD_ShowImage(image,0,0)	
=======
draw.rectangle((0,0,width,height), outline=0, fill=0)

draw.text((15, 10), 'Video Games', fill = "GREEN")
draw.text((15, 20), 'Apps & tools', fill = "GREEN")
disp.LCD_ShowImage(image,0,0)
i = 0
c = 0

while 1:
        draw.text((50, 50), str(c), fill = "GREEN")

        if GPIO.input(KEY_RIGHT_PIN) == 0:
                c += 11

        if i <= 0 :
                i = 1
        if i > 2 :
                i = 2
        if GPIO.input(KEY_UP_PIN) == 0:
                i -= 1
        if GPIO.input(KEY_DOWN_PIN) == 0:
                i += 1
        if i == 1: # button is released
                draw.text((15, 10), 'Video Games', fill = "GREEN")
        else:
                draw.text((15, 10), 'Video Games', fill = "BLUE")
        if i == 2:
                draw.text((15, 20), 'Apps & tools', fill = "GREEN")
        else:
                draw.text((15, 20), 'Apps & tools', fill = "BLUE")
        disp.LCD_ShowImage(image,0,0)
>>>>>>> 70c31e351b764085554467279c81f2ac6c5fd8ea
