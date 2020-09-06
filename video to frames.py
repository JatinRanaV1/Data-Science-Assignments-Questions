import cv2
import numpy as np
import os
from os.path import isfile, join
import shutil
import sys

video = input('Enter full path of video: ')
frameRate = int(input('Set frame rate: '))
pathIn, filename = os.path.split(os.path.realpath(video))
v = video.split('.')
ext = v[-1]
ff = ['mp4', 'mkv', 'wav', 'avi', 'gif', 'wmv', 'viv', '3gp']

if v[-1] not in ff: 
    print('File must be of video type.')

else:
    if isfile(video)==False:
        print('File not Found.')

    else:
        vidcap = cv2.VideoCapture(video)
        folder = pathIn + '\\frames'
        os.mkdir(folder)
    
        def getFrame(sec):
            vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = vidcap.read()
            if hasFrames:
                cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)
            return hasFrames

        sec = 0
        count=0
        success = getFrame(sec)
        while success:
            count = count + 1
            sec = sec + frameRate
            success = getFrame(sec)