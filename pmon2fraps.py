import csv
import sys
import math
import numpy as np



def avg(list):
    sum = 0
    for idx, elm in enumerate(list):
        sum += elm
    return round(sum/list.__len__(),4)


csvFile = open(sys.argv[1])
csvFrafs = open(sys.argv[1] + "_frafs.csv", 'wb')
# appName = sys.argv[2]
csvReader = csv.reader(csvFile)
csvData = list(csvReader)
subnetDict = {}
frame = 1
avg_fps = 0
pct_1_low = 0
pct_01_low = 0
ftimes = []
fftimes = []

frafsWriter = csv.writer(csvFrafs)
frafsWriter.writerow(['frame','frametime'])
frafsWriter.writerow([str(frame), '0.000'])
last = 0.0
totalft = 0.0
for row in csvData:
	# skip header
	if frame > 1:
		
		#grab MsBetweenPresents
		frametime = float(row[12])
		ftimes.append(float(row[12]))
		totalft += (float(row[12]))
		frafsWriter.writerow([str(frame), str(totalft)])
	frame += 1
   

avg_ftime = avg(ftimes)
low1 = np.percentile(ftimes, 99)
low01 = np.percentile(ftimes,99.9)
print "Average fps/ftime: " + str(round(1000.0/avg_ftime, 4)) + "fps - " + str(avg_ftime) + "ms"
print "1% low fps/ftime: " + str(round(1000.0/low1, 4)) + "fps - " + str(low1) + "ms"
print "0.1% low fps/ftime: " + str(round(1000.0/low01, 4)) + "fps - " + str(low01) + "ms"