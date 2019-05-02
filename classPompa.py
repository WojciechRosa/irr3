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
        self.gpio_rain_test = irr_config.gpio_rain_test
        self.gpio_water_test = irr_config.gpio_water_test
        self.gpio_main_switch = irr_config.gpio_main_switch
        self.gpio_sections_list = irr_config.gpio_sections_list

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.gpio_pump, GPIO.OUT)         # pomp initiation
        GPIO.output(self.gpio_pump, GPIO.HIGH)      # pump switch off

        GPIO.setup(self.gpio_rain_test, GPIO.IN)     # inicjacja czujnika deszczu
        GPIO.setup(self.gpio_water_test, GPIO.IN)    # inicjacja czujnika wody
        GPIO.setup(self.gpio_main_switch, GPIO.IN)   # inicjacja glownego przelacznika

        for section_id in self.gpio_sections_list:   # inicjacja sekcji podlewania
            GPIO.setup(section_id, GPIO.OUT)
            GPIO.output(section_id, GPIO.HIGH)      # reset of all section



    def status(self):
        print("status pompy  " + str(GPIO.input(self.gpio_pump)))
