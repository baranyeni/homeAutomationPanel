#!/usr/bin/env python

##import  RPi.GPIO as GPIO
from Tkinter import *
import requests

##
GPIO.setwarnings(False)
##GPIO.setmode(GPIO.BCM)

Light = 14
##GPIO.setup(Light, GPIO.OUT, initial=GPIO.LOW)

root = Tk()
root.config(cursor="none")
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

def ledOff():
     requests.get('http://192.168.1.27/LEDOff')

def ledOn():
    requests.get('http://192.168.1.27/LEDOn')

def lightOff():
     pass

def lightOn():
    pass

#Create a 5x10 (rows x columns) grid of buttons inside the frame
for row_index in range(0,2):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(0,2):
        Grid.columnconfigure(frame, col_index, weight=1)

        if (col_index == 0 and row_index == 0):
            openLedButton = Button(frame, text="Turn On LED", command=ledOn)
            openLedButton.grid(row=row_index, column=col_index, sticky=N+S+E+W)  

        if (col_index == 1 and row_index == 0):
            closeLedButton = Button(frame, text="Turn Off LED", command=ledOff)
            closeLedButton.grid(row=row_index, column=col_index, sticky=N+S+E+W)  

        if (col_index == 0 and row_index == 1):
            openLightButton = Button(frame, text="Turn On Light", command=lightOn)
            openLightButton.grid(row=row_index, column=col_index, sticky=N+S+E+W)  

        if (col_index == 1 and row_index == 1):
            closeLightButton = Button(frame, text="Turn Off Light", command=lightOff)
            closeLightButton.grid(row=row_index, column=col_index, sticky=N+S+E+W)  


closeLedButton.configure(font=("monospace", 16, "normal"), bg="red", fg="white", activebackground="red", activeforeground="white", highlightthickness="0")
openLedButton.configure(font=("monospace", 16, "normal"), bg="green", fg="white", activebackground="green", activeforeground="white", highlightthickness="0")
closeLightButton.configure(font=("monospace", 16, "normal"), bg="red", fg="white", activebackground="red", activeforeground="white", highlightthickness="0")
openLightButton.configure(font=("monospace", 16, "normal"), bg="green", fg="white", activebackground="green", activeforeground="white", highlightthickness="0")


root.mainloop()
