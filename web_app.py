# web_app.py


import subprocess
from flask import Flask , Response
import os.path
import os
import signal
import atexit
import datetime

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

gpio_pump = 17
gpio_rain_test = 2
gpio_water_test = 3
gpio_main_switch = 5
gpio_sections_list =[5, 6, 13, 19,22, 26]

GPIO.setup(gpio_water_test, GPIO.IN) 

app = Flask(__name__)

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

def add_command_to_file(cmd):
        hs = open("irr_cmd.log","r+")
        content=hs.read()
        hs.seek(0,0)
        hs.write(cmd +'\n'+content)
        hs.close()

@app.route('/')
def hello_world():
   # return html
   content=get_file('index.html')
   return Response(content, mimetype="text/html")

@app.route('/status')
def status():
    str='<b> informacja o statusie pompy </b><br>'
    str=str+"status wody " + 'woda ok ' if GPIO.input(gpio_water_test) else 'woda not ok'

    return str
    
    
@app.route('/<action>/<section>/<time>')
def action(action,section,time):

        if (action=='on' or action=="off") and int(section) <7 and int(time) < 31:
                #py_cmd = ' python irr_main3.py'
                py_cmd=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+';'
                if action == "on": py_cmd= py_cmd + "start;"+time+";"+ section
                if action == "off": py_cmd= py_cmd + "stop;"+time+";"+ section

        #subprocess.Popen(py_cmd, shell=True)
        add_command_to_file(py_cmd)

        content=get_file('index.html')
        return Response(content, mimetype="text/html")


if __name__ == '__main__':
    app.run(host="192.168.0.113")
