import string as s
import random as r
import time

for i in range(1,501):
    fp = open (str(i) + ".txt", "w")
    for j in range(20000):
        string = r.sample(s.ascii_letters, 20)
        string = "".join(string)
        fp.write(string + "\n")
    fp.close() 
    
file = open('Q2.csv','w')
file.write('No. of Files, Time Taken (sec)')

for files in range(100,501,100):
    start = time.time()
    for i in range(1, files+1):
        file_name = str(i)+'.txt'
        fp = open(file_name,'r')
        text = fp.read()
        fp.close()
        lines = [text.upper()]
        fp = open(file_name, 'w')
        fp.writelines(lines)
        fp.close()
        
    end = time.time()
    req_time = end - start
    string = str(files) + ',' + str(req_time)
    file.write('\n')
    file.write(string)
file.close()
