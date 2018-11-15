"""
Buttons
Button 1 (BCM 5): Arm/Unarm
Button 2 (BCM 6): Reset
Button 3, 4, 5 (BCM 17, 27, 22): PIN 

Buzzer (BCM 25): Alarm

LEDs
LED 1 (BCM 23): Armed/Unarmed Status
LED 2 (BCM 24): Alarm
"""

import gpiozero as io

btnArm = io.Button(5)
btnReset = io.Button(6)
btnPIN1 = io.Button(17)
btnPIN2 = io.Button(27)
btnPIN3 = io.Button(22)

buzzer = io.Buzzer(25)

ledStatus = io.LED(23)
ledAlarm = io.LED(24)

def main():
    while(True):
        if(btnPIN1.is_pressed or btnPIN2.is_pressed or btnPIN3.is_pressed):
            PIN = set_pin()
            while(True):
                btnArm.wait_for_press()
                #Armed
                ledStatus.on()
                if(btnPIN1.is_pressed or btnPIN2.is_pressed or btnPIN3.is_pressed):
                    if(check_pin(PIN)):
                        #PIN Matched, wait for btnArm again
                    else:
                        #Wrong PIN, sound the alarm
                        sound_alarm()


def set_pin():
    PIN = {0,0,0}
    for i in PIN:
        if(btnPIN1.is_pressed):
            PIN[i] = 1
        if(btnPIN2.is_pressed):
            PIN[i] = 2
        if(btnPIN3.is_pressed):
            PIN[i] = 3
    return PIN

def check_pin(PIN):
    userInput = {0,0,0}
    for i in userInput:
        if(btnPIN1.is_pressed):
            userInput[i] = 1
        if(btnPIN2.is_pressed):
            userInput[i] = 2
        if(btnPIN3.is_pressed):
            userInput[i] = 3

    return(userInput == PIN)

def sound_alarm():
    while(not btnReset.is_pressed):
        buzzer.toggle()
        ledAlarm.toggle()
