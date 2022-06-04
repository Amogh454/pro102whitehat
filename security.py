from os import access
from tkinter import Frame
import cv2
from cv2 import VideoCapture
import random
import dropbox

def snapshot():
    number = random.randint(0,100)
    VideoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = VideoCaptureObject.read()
        imgName = 'image'+str(number)+'.png'
        cv2.imwrite(imgName, frame)
        result = False

    return imgName

def uploadfile(imgName):
    accessToken = 'sl.BIsxEB2w6zMz6X4iH7k401pE9mX1vZ6qSAaQrcRnyMRfDocz_7TtNIeVcrT9ITgsxM1uRrpOn9jBcQxkkamWTb_sRm1U9U4OQZgjIGsAmqE1Jr3KE6sfdQXNItOmDtkxjZFLJgqTv7Zj'
    file = imgName
    source = file
    destination = '/cctv/'+(imgName)
    dbx = dropbox.Dropbox(accessToken)

    with open(source, 'rb') as f:
        dbx.files_upload(f.read(), destination, mode = dropbox.files.WriteMode.overwrite)
        print('successfully file uploaded...')

snap = snapshot()            

uploadfile(snap)



