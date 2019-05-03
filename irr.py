#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys, signal
from time import sleep
import datetime
from classPompa import class_pompa

p=class_pompa()

minutes=int(sys.argv[2])*6
sekcja=int(sys.argv[3])-1
i=0



print "\nStart programu \n", 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv) , '\n---------------------------------------------- '


# Main Program
while minutes>i:
        i += 1

        if p.water_test:
                print "end process: water test"
                p.stop()
                break

        if str(sys.argv[1]) == 'start':
                p.start()
                p.open_section(sekcja)
                sleep(10)
        else:
                p.stop()
                p.close_all_sections()
                break
        print(p.status)
        print(i)
