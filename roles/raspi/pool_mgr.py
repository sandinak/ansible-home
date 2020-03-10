#! env python

from gpiozero import LED
from time import sleep

# configuration of the pi
#  The relay hat uses GPIO pins 26, 19, 13, and 6 to control four relays.
pump1 = LED(26)
pump2 = LED(19)
pump3 = LED(13)
pump4 = LED(6)

while True:
    pump1.on()
    sleep(1)
    pump1.off()
    sleep(1)

    pump2.on()
    sleep(1)
    pump2.off()
    sleep(1)

    pump3.on()
    sleep(1)
    pump3.off()
    sleep(1)

    pump4.on()
    sleep(1)
    pump4.off()
    sleep(1)