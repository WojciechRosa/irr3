#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import signal
from time import sleep
import datetime
from classPompa import class_pompa

p=class_pompa()


try:
    minutes=int(sys.argv[2])*6
    number_of_args=len(sys.argv)
except:
    minutes=0
    number_of_args=0
i=0




print "\nStart programu \n", 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv) , '\n---------------------------------------------- '


# Main Program


# Part responsible for cross check if water is in well
# this part is run by crontab
if str(sys.argv[1]) == 'water_test':
    if p.water_test():
        p.reset()
        print("no water, system switch off")
    else:
        print("water ok")

    exit()

# main loop for watering
while minutes>=i:
    i += 1
    try:
                if p.water_test():
                        print "end process: water test"
                        p.stop()
                        quit()

                if str(sys.argv[1]) == 'start':
                        p.close_all_sections()
                        for x in xrange(3,number_of_args):
                            try:
                                sekcja=int(sys.argv[x])
                                p.open_section(sekcja)
                            except ValueError:
                                print(" Error of input parameters")
                                quit()
                        p.start()
                        sleep(10)
                elif str(sys.argv[1]) == 'status':
                        print(p.status())
                        break

                elif str(sys.argv[1]) == 'reset':
                        p.reset()
                        print(p.status())
                        break

                else:
                        p.stop()
                        p.close_all_sections()
                        break

                print(p.status())
                print(i)
    except KeyboardInterrupt:
        p.stop()
        print('stopped by CTRL+C')
        stored_exception=sys.exc_info()
        break
p.stop()
