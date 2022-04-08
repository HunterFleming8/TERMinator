from cmath import atan,acos,asin
from tkinter import *
from numpy import *
from PositioningScreen import xcoord,ycoord,zcoord
from LengthScreen import foreArm, upperArm
import serial
import time

#Base Angle
baseAngle=atan((ycoord)/(xcoord))
baseAngle_degrees=baseAngle*(180/pi)

r=sqrt((xcoord)**2+(ycoord)**2+(zcoord)**2)

#Elbow Angle in Radians
elbowAngle_1=((xcoord)**2+(ycoord)**2+(zcoord)**2-(foreArm)**2*(upperArm)**2)/(2*(foreArm)*(upperArm))
elbowAngle=-acos(elbowAngle_1)
elbowAngle_degrees=elbowAngle*(180/pi)

#Alpha Angle in Radians
alpha_1=(zcoord)/r
alpha=asin(alpha_1)

#Beta Angle in Radians
beta_1=((foreArm)*sin(elbowAngle))/((upperArm)+(foreArm)*cos(elbowAngle))
beta=arctan(beta_1)

#Shoulder Angle
shoulderAngle=alpha+beta
shoulderAngle_degrees=shoulderAngle*(180/pi)

def MotorAngles():
    global shoulderAngle_degrees
    global elbowAngle_degrees
    global baseAngle_degrees

print('Shoulder Angle is ',shoulderAngle_degrees)
print('Elbow Angle is ',elbowAngle_degrees)
print('Base Angle is ',baseAngle_degrees)

import serial
port='COM'    #Input what port the USB is connected to
pin1=2
pin2=4
pin3=3

servoB=serial.Serial(port,9600)
servoS=serial.Serial(port,9600)
servoE=serial.Serial(port,9600)

def moveMotorB(pin1,servoBPos):
    servoB.digital[pin1].write(servoBPos)
    while True:
        if pin1=='2':      #Input what pin the BASE motor is attached to
         servoBPos=baseAngle_degrees

def moveMotorS(pin2,servoSPos):
    servoS.digital[pin2].write(servoSPos)
    while True:
        if pin2=='4':       #Input what pin the SHOULDER motor is attached to
         servoSPos=shoulderAngle_degrees

def moveMotorE(pin3,servoEPos):
    servoE.digital[pin3].write(servoEPos)
    while True:
        if pin3=='3':       #Input what pin the ELBOW motor is attached to:
         servoEPos=elbowAngle_degrees




