
#!/usr/bin/python
# -*- coding: utf-8 -*-

# ----- IRRIGATION SIMPLE MODEL ------
# garden irrigation process run at time by crone
#
#
# Author: Wojciech Rosa
# Author email: wojciech.rosa@gmail.com
# Veriosn: 1.0
# Date: March 2017
# Status: on development

import sys, signal
from time import sleep
import datetime

#from classWaterPump import *

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)


gpio_pump = 17
gpio_rain_test = 2
gpio_water_test = 3
gpio_main_switch = 5
gpio_sections_list =[5, 6, 13, 19,22, 26]


GPIO.setup(gpio_pump, GPIO.OUT)         #inicjacja pompy
GPIO.output(gpio_pump, GPIO.HIGH)

GPIO.setup(gpio_rain_test, GPIO.IN)     #inicjacja czujnika deszczu
GPIO.setup(gpio_water_test, GPIO.IN)    #inicjacja czujnika wody
GPIO.setup(gpio_main_switch, GPIO.IN)   #inicjacja głównego przelacznika


for section_id in gpio_sections_list:   #inicjacja sekcji podlewania
    GPIO.setup(section_id, GPIO.OUT)
    GPIO.output(section_id, GPIO.HIGH)
    #print "open gipo pin: ", section_id

class ClassPompa():
        def stop(self):
                GPIO.output(gpio_pump, GPIO.HIGH)
                self.close_all_sections()
        def start(self,section):

                GPIO.output(gpio_pump, GPIO.LOW)
                GPIO.output(gpio_sections_list[section-1],GPIO.LOW)
        def close_all_sections(self):
                for section_id in gpio_sections_list:
                        GPIO.output(section_id, GPIO.HIGH)
        def water_test():
                return GPIO.input(gpio_water_test)

Pompa=ClassPompa()  #inicjacja klasy pomopy

while True:
    try:

        sleep(1)

        if not Pompa.water_test:
                print("brak wody w studni")
                quit()


        f=open('irr_cmd.log','r')
        date_time,cmd,minutes,section =f.readline().split(';')
        time_delta=int(minutes)*60

        date_time_start = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M$
        date_time_stop=date_time_start+datetime.timedelta(seconds=time_delta)

        print(date_time, cmd, minutes, section)

        if date_time_stop>=datetime.datetime.now():
                print('działa')
                if cmd=='start': Pompa.start(int(section))
                if cmd!='start': Pompa.stop()
                
        else:

                print('nie działa')
                Pompa.stop()
                print(date_time_stop)

    except KeyboardInterrupt:
        except KeyboardInterrupt:
        GPIO.output(gpio_pump, GPIO.HIGH) #wyłączenie pompy
        print('stopped by CTRL+C')
        stored_exception=sys.exc_info()
        break

quit()

minutes=int(sys.argv[2])*6
sekcja=int(sys.argv[3])-1
i=0

#-----------------------------------------------------------

print "Start programu"
print " "
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print " "
print "------------------"


# Main Program
while minutes>i:
        i+=1

        if str(sys.argv[1]) == 'stop':
                GPIO.output(gpio_pump, GPIO.HIGH)

                for section_id in gpio_sections_list:
                        GPIO.output(section_id, GPIO.HIGH)
                break

        if GPIO.input(gpio_water_test):
                print "end process: water test"
                break

        if not GPIO.input(gpio_rain_test):
                print "end process:     rain test"
                break


        if str(sys.argv[1]) == 'start':
                GPIO.output(gpio_pump, GPIO.LOW)
                GPIO.output(gpio_sections_list[sekcja], GPIO.LOW)
                sleep(10)

        now = datetime.now()
        
        
        print "---- praca -------"
        print str(now)
        print "pump status:" + str(GPIO.input(gpio_pump))
        print "sekcja:     " +str(sekcja)
        print "rain test:" + str(GPIO.input(gpio_rain_test))
        print "water test:" + str(GPIO.input(gpio_water_test))
        print "main switch test:" + str(GPIO.input(gpio_main_switch))
        print " "

print "------------------"
GPIO.cleanup()








