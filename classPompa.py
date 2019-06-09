
import irr_config
import RPi.GPIO as GPIO
from datetime import datetime



class class_pompa(object):
    def __init__(self):
        self.gpio_pump = irr_config.gpio_pump
        self.gpio_rain_test = irr_config.gpio_rain_test
        self.gpio_water_test = irr_config.gpio_water_test
        self.gpio_main_switch = irr_config.gpio_main_switch
        self.gpio_sections_list = irr_config.gpio_sections_list
        self.file_test_log = irr_config.file_test_log
        self.file_action_log = irr_config.file_action_log

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.gpio_pump, GPIO.OUT)         # pomp initiation

        GPIO.setup(self.gpio_rain_test, GPIO.IN)     # inicjacja czujnika deszczu
        GPIO.setup(self.gpio_water_test, GPIO.IN)    # inicjacja czujnika wody
        GPIO.setup(self.gpio_main_switch, GPIO.IN)   # inicjacja glownego przelacznika

        for section_id in self.gpio_sections_list:   # inicjacja sekcji podlewania
            GPIO.setup(section_id, GPIO.OUT)

    def reset(self):
        GPIO.output(self.gpio_pump, GPIO.HIGH)      # pump switch off
        for section_id in self.gpio_sections_list:   # inicjacja sekcji podlewania
            GPIO.output(section_id, GPIO.HIGH)      # reset of all section
        GPIO.cleanup()


    def status(self):
        txt = "    status pompy \n"
        txt = txt + "    Pompa:          " + ("stop" if GPIO.input(self.gpio_pump) else "praca") + " \n"
        txt = txt + "    Woda w sudni:   " + ("jest woda" if not GPIO.input(self.gpio_water_test) else "brak wody") + " \n"

        for section in self.gpio_sections_list:
            txt = txt + "    Sekcja [" + ("0" if section < 10 else "") + str(section) + "]:    " + ("zamknieta" if GPIO.input(section) else "otwarta") + " \n"
        return txt

    def open_section(self, section):   # open section
        GPIO.output(self.gpio_sections_list[section-1], GPIO.LOW)

    def close_section(self, section):   # close section
        GPIO.output(self.gpio_sections_list[section-1], GPIO.HIGH)

    def stop(self):   # stop pompa
        GPIO.output(self.gpio_pump, GPIO.HIGH)

    def start(self):   # start pompa
        GPIO.output(self.gpio_pump, GPIO.LOW)

    def close_all_sections(self):
        for section_id in self.gpio_sections_list:
            GPIO.output(section_id, GPIO.HIGH)          #close all sections
    def water_test(self):
        return  GPIO.input(self.gpio_water_test)

    def add_to_log(self, log_file, log_text):
        now = datetime.now() # current date and time
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        f = open(log_file,"a+")

        log_text = date_time + "   " + log_text +"\n"
        f.seek(0)
        f.write(log_text)
        f.close()

