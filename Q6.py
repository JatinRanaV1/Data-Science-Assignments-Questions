import numpy as np
import pandas as pd
import sys
import time
import os
from os.path import isfile, join
import csv

if len(sys.argv)<2:
    print('Incorrect number of parameters.')

else:
    count=0
    for i in range(1, len(sys.argv)):
        file = sys.argv[i]
        f = file.split('.')
        e = f[-1]
        if e!='csv' and e!='txt':
            count+=1
    if count!=0:
        print('File must be of csv or txt type.')
    else:
        for i in range(1, len(sys.argv)):
            if isfile(sys.argv[i])==False:
                count+=1
        if count!=0:
             print('File not Found.')
        else:  
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)
            output=pd.DataFrame()
            log=pd.DataFrame()
            F1=[]
            F2=[]
            F3=[]
            F4=[]
            F5=[]
            F6=[]
            Class=[]
            for i in range(1, len(sys.argv)):
                file = sys.argv[i]
                f = file.split('.')
                e = f[-1]
                s=[]
                f=[]
                df=pd.read_csv(sys.argv[i])
                for k in range (len(df)):
                    if df['Class'][k] == '+':
                        df['Class'][k]=1
                    if df['Class'][k] == '-':
                        df['Class'][k]=0
                for k in range(len(df)):
                    if hasNumbers(df['Sequence'][k])==True:
                        s.append(df['Sequence'][k])
                        f.append(sys.argv[i])
                    else:
                        n,h,q,g,d,t=0,0,0,0,0,0
                        for j in df['Sequence'][k]: 
                            if j=='N':
                                n+=1
                            if j=='H':
                                h+=1
                            if j=='Q':
                                q+=1
                            if j=='G':
                                g+=1
                             if j=='D':
                                d+=1
                             if j=='T':
                                t+=1
                        F1.append(n)
                        F2.append(h)
                        F3.append(q)
                        F4.append(g)
                        F5.append(d)
                        F6.append(t)
                        Class.append(df['Class'][k])
            output['F1']=F1
            output['F2']=F2
            output['F3']=F3
            output['F4']=F4
            output['F5']=F5
            output['F6']=F6
            output['Class']=Class
            output=output.reset_index()
            output=output.rename(columns={'index':'SN'})
            for k in range(len(output)):
                output['SN'][k]+=1
            log['File Name']=f
            log['Sequence']=s

            t = time.time()
            output.to_csv('result-'+str(t)+'.csv')
            log.to_csv('log-'+str(t)+'.csv')
            
            time = time.strftime("%Y%m%d", time.localtime(time.time()))
            input_file = 'log-'+str(t)+'.csv'
            output_file = 'log-'+str(time)+'.csv'
            row_count = 0

            with open(input_file, "r") as source:
                reader = csv.reader(source)
                with open(output_file, "w", newline='') as o:
                    writer = csv.writer(o)
                    for row in reader:
                        row_count += 1
                        del row[0]
                        writer.writerow(row)

            input_file = 'result-'+str(t)+'.csv'
            output_file = 'result-'+str(time)+'.csv'
            row_count = 0

            with open(input_file, "r") as source:
                reader = csv.reader(source)
                with open(output_file, "w", newline='') as o:
                    writer = csv.writer(o)
                    for row in reader:
                        row_count += 1
                        del row[0]
                        writer.writerow(row)
             
            os.remove('result-'+str(t)+'.csv')
            os.remove('log-'+str(t)+'.csv')
