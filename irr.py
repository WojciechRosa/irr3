#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys, signal
from time import sleep
import datetime
from classPompa import class_pompa

p=class_pompa()

try:
    minutes=int(sys.argv[2])*6
    sekcja=int(sys.argv[3])
except
    minutes=0
    sekcja=0
i=0



print "\nStart programu \n", 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv) , '\n---------------------------------------------- '


# Main Program
while minutes>i:
    i += 1
    try:
                if p.water_test():
                        print "end process: water test"
                        p.stop()

                if str(sys.argv[1]) == 'start':
                        p.start()
                        p.open_section(sekcja)
                        sleep(10)
                elif str(sys.argv[1]) == 'status':
                        print(p.status())
                
                elif str(sys.argv[1]) == 'reset':
                        p.reset()
                        print(p.status())
                
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
