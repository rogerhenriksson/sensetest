from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
yellow = (255,255,0)
blue = (0,0,255)
sense.show_message("Hello, world!",0.05,yellow,blue);

sense.clear((0,0,0))
sleep(0.5)

sense.show_letter("D",text_colour=(randint(0,255),randint(0,255),randint(0,255)))
sleep(0.5)
sense.show_letter("i",text_colour=(randint(0,255),randint(0,255),randint(0,255)))
sleep(0.5)
sense.show_letter("s",text_colour=(randint(0,255),randint(0,255),randint(0,255)))
sleep(0.5)
sense.show_letter("p",text_colour=(randint(0,255),randint(0,255),randint(0,255)))
sleep(0.5)
sense.show_letter("l",text_colour=(randint(0,255),randint(0,255),randint(0,255)))
sleep(0.5)
sense.show_letter("a",text_colour=(randint(0,255),randint(0,255),randint(0,255)))
sleep(0.5)
sense.show_letter("y",text_colour=(randint(0,255),randint(0,255),randint(0,255)))
sleep(0.5)
sense.show_letter("O",text_colour=(randint(0,255),randint(0,255),randint(0,255)))
sleep(0.5)
sense.show_letter("K",text_colour=(randint(0,255),randint(0,255),randint(0,255)))
sleep(0.5)

sense.clear((0,0,0))
sense.set_pixel(0,0,(255,0,0))

print("Pressure:",sense.get_pressure())

print("Temp (humidity sensor):",sense.get_temperature_from_humidity())
print("Temp (pressure sensor):",sense.get_temperature_from_pressure())

print("Humidity:",sense.get_humidity())

print("Orientation:",sense.get_orientation())
print("Acceleration:",sense.get_accelerometer_raw())

print("Please move joystick!")
while True:
    for event in sense.stick.get_events():
        print(event.direction,event.action)
    
