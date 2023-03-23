# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:55:58 2023

@author: waghmare
"""

import serial
from pynput.keyboard import Key,Controller
                                                                     
keyboard =Controller()                                                                               

ser = serial.Serial(
    port='COM15',
    baudrate=115200,
)

while(True):                      
    if(ser.readline()==b'1\r\n'):
        keyboard.press(Key.space)                                                                                                                                                                                                                                  
    else:
        print("b'0/r/n'")

ser.close()   
                                        