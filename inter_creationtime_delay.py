######################## LDM Latency and Throughput Log File Parser  ##############################
# Usage: python inputfile 
# Example: python ldmd.log 
# Author:Xiang Ji; Modified by Joseph Slezak
# Email: xj4hm@virginia.edu; jjs358@scarletmail.rutgers.edu
################################################################################


import csv
import sys

from datetime import datetime
# A function to convert the time string to datetime object then calculate the time difference
def between_time(a, b):
	s1 = a
	s2 = b
#	FMT1 = "%Y-%m-%dT%H:%M:%S.%f-04:00"
	FMT2 = "%Y%m%d%H%M%S.%f"
	difference = datetime.strptime(s1, FMT2) - datetime.strptime(s2, FMT2)

	#A timedelta object has days, seconds, microseconds. Convent to miliseconds
        return (difference.days * 24 * 3600 * 1000000 + difference.seconds * 1000000 + difference.microseconds) / 1000 
##a = datetime.strptime("2014-11-18T09:20:44.404740-05:00","%Y-%m-%dT%H:%M:%S.%f-05:00")
##b = datetime.strptime("20141118142043.687","%Y%m%d%H%M%S.%f")

inputfile = sys.argv[1]

outputfile = inputfile + '.analysis.csv'
writer = csv.writer(open(outputfile, 'wb', buffering=0))
writer.writerow(['Time_Between_Products(ms)'])


f = open(inputfile, 'r')

counter = 0

# !!! Set prevLine below to something just before the first line in the logfile 
# !!! and remember to ignore/delete the first line in the .pqanalysis.csv output
prevLine = "115831 20150614235959.984"


for line in f:
    currentlist = line.split()
    prevLineSplit = prevLine.split()
    
    if currentlist[0].isdigit():
        
        counter = counter + 1
        print 'Working on Row:', counter
                        
        delay = between_time((currentlist[1]),(prevLineSplit[1]))
        
        writer.writerow([float(delay)])
        
    prevLine = line
               
f.close()



