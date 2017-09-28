#Whenever founds internet connectivity  confirms is it you if not log you off
#and send pic of intruder to your Pushbullet connected all devices.

#Author :  Vishal Kumar
#https://github.com/TheBeast007/

import cv2
import numpy as np
from pushbullet import PushBullet
import win32com.client as wincl
import time
import os


#takes intruder pic
def intruder_pic():
 cam=cv2.VideoCapture(0)
 s,im=cam.read()
 #cv2.imshow("Test Picture",im)
 cv2.imwrite("Intruder.bmp",im)


#intruder suspected message
def suspected_message():
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("Intruder Suspected")

#Your PushBullet API key
api_key ="YourPushBulletAPIKeyHere"
pb =PushBullet(api_key)
pushMsg =pb.push_note("PYTHON : ","Found Internet Connectivity, is this you? if not message 'No' ")


#pushes captured image to Mobile
def Image_send():
    with open("Intruder.bmp", "rb") as pic:
        file_data = pb.upload_file(pic, "Intruder.bmp")

    push = pb.push_file(**file_data)

#log off PC if Intruder Suspected
def logOff():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



#Controller
def Control():
    while True:
     val =pb.get_pushes()
     action =val[0]['body']
     print(action)
     if action=='No' or 'no':
        suspected_message()
        intruder_pic()
        Image_send()
        time.sleep(15)
        logOff()
     else:
        pass


Control()
