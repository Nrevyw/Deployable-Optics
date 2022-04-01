from functools import partial
import serial
import numpy as np
import time
from labjack import ljm
from datetime import datetime
import os
from inspect import getsourcefile
import winsound

class labjack:
    def connect():
        return ljm.openS("T7","ANY","ANY")

    def read(handle,ain):
        return ljm.eReadName(handle, ain)/10

class GT2:
    def init(COMport):
            baudrate = 38400; % baudrate for Keyence GT2-UB
            return serial.Serial(COMport,baudrate,timeout=5)

    def read(device):
        command = 'SR,00,000'
        device.write(command.encode('ascii'))
        time.sleep(1)
        return device.readline()

        # ADD POST PROCESSING BIT HERE
            strvalue = extractAfter(valuereturn,strcat(command,","));
            value = str2double(strvalue);

## Number of Deployments
n = 1
num = np.linspace(1,n,n)                        # CHANGE NUM OF DEPL.


## For loop for measurement

path_to_script = os.path.dirname(getsourcefile(lambda:0))
my_filename = os.path.join(path_to_script, r"PLACEHOLDER.txt")
print('Log found at '+my_filename)

handle = labjack.connect()

time.sleep(5)
for i in num:
    wait = input('Deploy, then hit Enter')
    time.sleep(1)                              # CHANGE VIBRATION TIME
    now = datetime.now()
    timenum=now.strftime("%H:%M:%S")
    AIN0 = labjack.read(handle,'AIN0')
    AIN1 = labjack.read(handle,'AIN1')
    AIN2 = labjack.read(handle,'AIN2')


    with open(my_filename, "a") as log:
        log.write("{0},{1},{2}\n".format(timenum,AIN0,AIN1))

    winsound.Beep(2500,1000)

    time.sleep(2)







