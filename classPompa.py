"""
Doc String
Author: Wojceic Rosa

Class: Pompa

"""

import irr_config
import RPi.GPIO as GPIO


class class_pompa(object):
    def __init__(self):
        self.gpio_pump = irr_config.gpio_pump

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pump, GPIO.OUT)         # pomp initiation

    def status(self):
        print("status pompy" + str(self.gpio_pump))
