import time
from numpy import mean
from decimal import *
from subprocess import call

dataStat = []

f = open('stat_data.txt')
for line in f:
  dataStat.append(int(line))
f.close()

#print dataStat
max_val = max(dataStat)
# print 'max : ' + str(max_val)

min_val = min(dataStat)
# print 'min : ' + str(min_val)

date_str = time.strftime("_%Y-%m-%d_%H_%M_%S", time.localtime())
cp_filename = 'update_date' + date_str + '.txt'
# print cp_filename

cp_cmd = 'cp log_for_health_check.txt ' + cp_filename
# print cp_cmd
# cp_filename = "update_%{time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())}.txt"
#print time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())

# call(cp_cmd, shell=True) #debug only

if max_val == 2:
  if max_val > min_val:
    call(cp_cmd, shell=True)
  else:
    call("rm log_for_health_check.txt", shell=True)
else:
    call(cp_cmd, shell=True)
