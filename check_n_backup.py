import time
from numpy import mean
from decimal import *
from subprocess import call

dataStat = []

f = open('/tmp/stat_data.txt')
for line in f:
  dataStat.append(int(line))
f.close()

#print dataStat
max_val = max(dataStat)
# print 'max : ' + str(max_val)

min_val = min(dataStat)

date_str = time.strftime("_%Y-%m-%d_%H_%M_%S", time.localtime())
cp_filename = '/media/sdcard/update_date' + date_str + '.txt'

cp_cmd = 'cp /tmp/log_for_health_check.txt ' + cp_filename
cp_cmd1 = 'uptime >> ' + cp_filename
cp_cmd2 = 'mv ' + cp_filename + ' /media/sdcard/archived'

if max_val == 2:
  if max_val > min_val:
    call(cp_cmd, shell=True)
    call(cp_cmd1, shell=True)
    f = open('/tmp/halt.txt')
    for line in f:
        dataStat.append(int(line))
    f.close()
    max_val = max(dataStat)
    if max_val == 2:
        call(cp_cmd2, shell=True)
  else:
    call("rm /tmp/log_for_health_check.txt", shell=True)
else:
    call(cp_cmd, shell=True)
