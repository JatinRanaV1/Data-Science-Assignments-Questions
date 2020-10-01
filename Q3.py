import cv2
import numpy as np
import os
from os.path import isfile, join
import shutil
import sys

if len(sys.argv)!=2:
    print('Incorrect number of parameters.')

else:
    video = sys.argv[1]
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
            folder = pathIn + '\\test'
            os.mkdir(folder)

            def getFrame(sec):
                vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
                hasFrames,image = vidcap.read()
                if hasFrames:
                    cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    cv2.imwrite(pathIn+"/test/frame{:d}.jpg".format(count), gray)
                return hasFrames

            sec = 0
            frameRate = 0.04
            count=0
            success = getFrame(sec)
            while success:
                count = count + 1
                sec = sec + frameRate
                success = getFrame(sec)

            v=''.join(v[:-1])
            pathOut = v+'_output.'+ext
            frame_array = []

            for i in range(0,count):
                filename=pathIn + '/test/frame%d.jpg' %i
                img = cv2.imread(filename)
                height, width, layers = img.shape
                frame_array.append(img)

            shutil.rmtree(folder, ignore_errors=True)

            out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), 25, (width, height))

            for i in range(0,count):
                out.write(frame_array[i])
            out.release()
