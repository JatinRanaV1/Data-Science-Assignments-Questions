## Q1. WAP to sort the following number of elements in a list and calculate time taken.
#### Number of elements in list: 5k, 10k, 15k, 20k, 25k	    
#### Time Taken to sort: T1, T2, T3, T4, T5

## Q2. Create 500 txt files in a directory. Every file contains 20,000 lines and every line contain random string of length 20 characters. And then calculate the execution time to convert all the file to upper case. Save the results in csv file as given below.
#### Number of Files, Time Taken (sec)
             100, T1
             200, T2
             300, T3
             400, T4
             500, T5

## Q3. Develop a command line program to convert a Video File to Black & White.
### Run the program through command line: python Q3.py VideoFileName
  
## Q4. Develop a command line program to resize a Video File.
### Run the program through command line: python Q3.py VideoFileName X (here X is resize percentage between 1 to 99)
#### Input/Output: 
##### • Input File Name  video.mp4
##### • Output File Name  video_output.mp4

## Q5. Develop a command line program to merge all the results available in multiple files.
### Description:
##### • Column names may be different in input files, but first column is id/roll-num and second column is marks.
##### • Input file(s) may contain duplicate roll numbers, you need to consider the last entry only.
e.g. In Case I, the file A.csv contain two values for roll no 100. You need to considered only last entry for roll no 100 i.e. 1.
##### • Put “0” (Zero) for missing values.
###### e.g. In Case I the file A.csv contain no entry for roll no 105 and 106. You need to put “0” (Zero) in output file in Column “A”.
###### e.g. In Case I the file C.csv contain no entry for roll no 102. You need to put “0” (Zero) in output file in Column “C”.
##### • In Case II, If only one input file is present, then remove duplicate entries and considered only last entry.
##### • Marks must be of numeric type (Except for missing value). For the non-numeric value of marks, make the entry of File Name, Roll No and Marks in the log file.
#### • Hint: Find the union of all roll numbers, available in all input files.
### Run the program through command line: python Q5.py File1 File2 ………… FileN
#### Result file: Merged result file
##### ▪ “result-” + str(time.time()) + “.csv”
##### ▪ e.g. → “result-20200909.csv”
#### Log file: Non numeric entry for marks with file name, roll no and marks.
##### • “log-” + str(time.time()) + “.csv”
##### • e.g. → “log-20200909.csv”
##### A.csv, 102012, ab
##### B.csv, 102, x
##### B.csv, 119, ‘y’

## Q6. Develop a command line program to extract the features of a protein sequence file.
### Description:
#### • Input file contain only two columns: first column is the protein sequence and second column is class (either -ve or +ve).
#### • Extract the feature of the sequence as given rule:
##### --- SN = SN of sequence
##### --- F1 = Count the number of N in sequence
##### --- F2 = Count the number of H in sequence
##### --- F3 = Count the number of Q in sequence
##### --- F4 = Count the number of G in sequence
##### --- F5 = Count the number of D in sequence
##### --- F6 = Count the number of T in sequence
##### --- Class = Replace '+ with 1' and '- with 0'
### Run the program through command line: python Q5.py File1 File2 ………… FileN
#### Result file: Merged result file
##### ▪ “result-” + str(time.time()) + “.csv”
##### ▪ e.g. → “result-20200909.csv”
#### Log file: Non numeric entry for marks with file name, roll no and marks.
##### • “log-” + str(time.time()) + “.csv”
##### • e.g. → “log-20200909.csv”
##### file1.csv, AGERT5DCT
##### file1.csv, AR45GVT
##### file2.txt, ASDR9RT
##### file3.txt, A4ADER
