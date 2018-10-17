import time
from numpy import mean
from decimal import *
from subprocess import call

# call("echo Hello World", shell=True)
# call("ls -la", shell=True)
# call("cp file.txt /media/sdcard", shell=True)

dataStat = []

f = open('stat_data.txt')
for line in f:
  dataStat.append(int(line))
f.close()

#print dataStat

max_val = max(dataStat)
print 'max : ' + str(max_val)

min_val = min(dataStat)
print 'min : ' + str(min_val)

if max_val == 2:
  if max_val > min_val:
#    print 'Wrong'
    call("cp log_for_health_check.txt file01.txt", shell=True)
  else:
#    print 'Correct'
    call("rm log_for_health_check.txt", shell=True)
