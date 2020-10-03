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
    file={}
    f={}
    count=0
    for i in range(1, len(sys.argv)):
        file[i] = sys.argv[i]
        f[i] = file[i].split('.')
        e = f[i][-1]
        if e!='csv':
            count+=1
    if count!=0:
        print('File must be of csv type.')
    else:
        for i in range(1, len(sys.argv)):
            if isfile(sys.argv[i])==False:
                count+=1
        if count!=0:
             print('File not Found.')
        else:
            df={}
            r={}
            rr={}
            for i in range(1, len(sys.argv)):
                df[i] = pd.read_csv(sys.argv[i])
                df[i].columns = ['Roll No', 'Marks']
                df[i] = df[i].fillna(0)
                r[i] = df[i][pd.to_numeric(df[i]['Marks'], errors='coerce').notnull()]
                rr[i] = df[i][pd.to_numeric(df[i]['Marks'], errors='coerce').isnull()]
                r[i] = r[i].groupby('Roll No').nth(-1)
                r[i] = r[i].reset_index()
                rr[i] = rr[i].reset_index()
                del rr[i]['index']
                
            l=[]
            for i in range(1, len(sys.argv)):
                for j in r[i].iloc[:, 0]:
                    if j not in l:
                        l.append(j)
            l.sort()
            result = pd.DataFrame() 
            result['Roll No'] = l
            result = result.set_index('Roll No')
            for i in range(1, len(sys.argv)):
                r[i] = r[i].set_index('Roll No')
                result[str(sys.argv[i][:-4])] = r[i].loc[:, 'Marks']
            result = result.reset_index()
            result = result.fillna(0)
            
            l=[]
            ll=[]
            lll=[]
            log = pd.DataFrame()
            for i in range(1, len(sys.argv)):
                for j in range(len(rr[i])):
                    l.append(sys.argv[i])
                    ll.append(rr[i].loc[j,'Roll No'])
                    lll.append(rr[i].loc[j,'Marks'])
            log['File Name'] = l
            log['Roll No'] = ll
            log['Marks'] = lll
            
            t = time.time()
            result.to_csv('result-'+str(t)+'.csv')
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
