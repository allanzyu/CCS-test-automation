#Author:Rusita Desai
#12/12/17
#Rev:1.0


import serial
import time
import os
import json
##import matplotlib.pyplot as plt
##import numpy as np

print"GDS2204E Remote Data"
CH1 = []
CH2 = []
CH3 = []
CH4 = []
Time_Stamp = []
f = open("output.txt", "w")
#f.write("Time                                           CH1           CH2              CH3              CH4\n")


Pressure_Ctrl = raw_input("Pressure Controller Model: ")
Mensor_Com_Port = float(raw_input("Please enter Mensor Serial Port: "))
set_pnt = float(raw_input("Please enter pressure set point: "))
step = float(raw_input("Please enter pressure step: "))
mensor_chan = raw_input("Mensor Chan: ")

mensor = serial.Serial()
mensor.baudrate = 57600
mensor.bytesize = 8
mensor.stopbits = 1
mensor.xonxoff = 0
mensor.rtscts = 0
mensor.timeout = None
mensor.port = Mensor_Com_Port
parity=serial.PARITY_NONE
mensor.open()
print "Connection to Mensor successful"
mensor.write("CMDSET MENSOR\n")
time.sleep(2)
mensor.write("CHAN " +str(mensor_chan)+"\n")
time.sleep(2)



duration = float(raw_input("Duration of test(hours): "))
increment = float(raw_input("Measurement increments(sec): "))
GDS_Com_Port = float(raw_input("Please enter GDS Serial Port (port-1): "))


print "Connecting to GDS2204E..."
ser = serial.Serial()
ser.baudrate = 9600
ser.bytesize = 8
ser.stopbits = 1
ser.xonxoff = 0
ser.rtscts = 0
ser.timeout = None
ser.port = GDS_Com_Port
parity=serial.PARITY_NONE
ser.open()
print "Connection to GDS2204E successful"
ser.write("*IDN?\n")
time.sleep(2)

print ser.readline()
ser.write(":CHANnel1:DISPlay ON\n")
ser.write(":CHANnel2:DISPlay ON\n")
ser.write(":CHANnel3:DISPlay ON\n")
ser.write(":CHANnel4:DISPlay ON\n")

startTime = time.asctime(time.localtime(time.time()))
##print time.time()
test_duration = duration * 60 * 60
Meas_Increment = test_duration/increment

for i in range(int(Meas_Increment)):
    mensor.write("SETPT "+str(set_pnt)+"\n")
    time.sleep(2)
    mensor.write("CONTROL\n")
    
    time.sleep(increment)
    time_stamp = time.asctime(time.localtime(time.time()))

    mensor.write("MEAS:PRES?\n")
    time.sleep(2)
    pressure= mensor.readline()
    
    ser.write(":MEASUrement:MEAS1:SOUrce1 CH1\n")
    ser.write(":MEASUrement:MEAS1:TYPe MEAN\n")
    ser.write(":MEASUrement:MEAS1:STATE ON\n")
    ser.write(":MEASUrement:MEAS1:VALue?\n")
    time.sleep(1)
    chan1 = ser.readline()
    CH1.append(chan1)

    ser.write(":MEASUrement:MEAS1:SOUrce1 CH2\n")
    ser.write(":MEASUrement:MEAS1:TYPe MEAN\n")
    ser.write(":MEASUrement:MEAS1:STATE ON\n")
    ser.write(":MEASUrement:MEAS1:VALue?\n")
    time.sleep(1)
    chan2 = ser.readline()
    CH2.append(chan2)

    ser.write(":MEASUrement:MEAS1:SOUrce1 CH3\n")
    ser.write(":MEASUrement:MEAS1:TYPe MEAN\n")
    ser.write(":MEASUrement:MEAS1:STATE ON\n")
    ser.write(":MEASUrement:MEAS1:VALue?\n")
    time.sleep(1)
    chan3 = ser.readline()
    CH3.append(chan3)

    ser.write(":MEASUrement:MEAS1:SOUrce1 CH4\n")
    ser.write(":MEASUrement:MEAS1:TYPe MEAN\n")
    ser.write(":MEASUrement:MEAS1:STATE ON\n")
    ser.write(":MEASUrement:MEAS1:VALue?\n")
    time.sleep(1)
    chan4 = ser.readline()
    CH4.append(chan4)

    print repr(time_stamp).rjust(2),repr(pressure).rjust(3), repr(chan1).rjust(4), repr(chan2).rjust(5), repr(chan3).rjust(6), repr(chan4).rjust(7)
    f.write(repr(time_stamp).rjust(2) + repr(pressure).rjust(3) + repr(chan1).rjust(4) + repr(chan2).rjust(5) + repr(chan3).rjust(6) + repr(chan4).rjust(7) + "\n")
    
    mensor.write("VENT\n")
    time.sleep(15)
    mensor.write("MEAS:PRES?\n")
    time.sleep(2)
    pressure= mensor.readline()
    time_stamp = time.asctime(time.localtime(time.time()))
    
    ser.write(":MEASUrement:MEAS1:SOUrce1 CH1\n")
    ser.write(":MEASUrement:MEAS1:TYPe MEAN\n")
    ser.write(":MEASUrement:MEAS1:STATE ON\n")
    ser.write(":MEASUrement:MEAS1:VALue?\n")
    time.sleep(1)
    chan1 = ser.readline()
    CH1.append(chan1)

    ser.write(":MEASUrement:MEAS1:SOUrce1 CH2\n")
    ser.write(":MEASUrement:MEAS1:TYPe MEAN\n")
    ser.write(":MEASUrement:MEAS1:STATE ON\n")
    ser.write(":MEASUrement:MEAS1:VALue?\n")
    time.sleep(1)
    chan2 = ser.readline()
    CH2.append(chan2)

    ser.write(":MEASUrement:MEAS1:SOUrce1 CH3\n")
    ser.write(":MEASUrement:MEAS1:TYPe MEAN\n")
    ser.write(":MEASUrement:MEAS1:STATE ON\n")
    ser.write(":MEASUrement:MEAS1:VALue?\n")
    time.sleep(1)
    chan3 = ser.readline()
    CH3.append(chan3)

    ser.write(":MEASUrement:MEAS1:SOUrce1 CH4\n")
    ser.write(":MEASUrement:MEAS1:TYPe MEAN\n")
    ser.write(":MEASUrement:MEAS1:STATE ON\n")
    ser.write(":MEASUrement:MEAS1:VALue?\n")
    time.sleep(1)
    chan4 = ser.readline()
    CH4.append(chan4)

    print repr(time_stamp).rjust(2),repr(pressure).rjust(3), repr(chan1).rjust(4), repr(chan2).rjust(5), repr(chan3).rjust(6), repr(chan4).rjust(7)
    f.write(repr(time_stamp).rjust(2) + repr(pressure).rjust(3) + repr(chan1).rjust(4) + repr(chan2).rjust(5) + repr(chan3).rjust(6) + repr(chan4).rjust(7) + "\n")

    
ser.close()
mensor.close()
