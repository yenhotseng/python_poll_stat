#!/bin/bash

# remove the previous test logs -- stat_data.txt and log_for_health_check.txt
if [ -a stat_data.txt ]
then rm stat_data.txt
  echo removed old log file
fi

if [ -a log_for_health_check.txt ]
then rm log_for_health_check.txt
  echo removed old log file
fi

echo sampling......
for i in {1..3000}
#this script runs on bud for about 30 secs, it means about 60 samples/sec, 1 sample/waveform
 do
   cat /sys/bus/iio/devices/iio\:device0/sampling_frequency >> log_for_health_check.txt
   sleep 0.00
 done
#sed 's/.*debug=\(.*\),\(.*\)/\1 \2/' log_for_health_check.txt | python pllstats.py
# sed 's/.*debug=\(.*\),\(.*\)/\1 \2/' log_for_health_check.txt 
#sed 's/.*state=\(.*[0-9]\)/\1/' | sed 's/ *halt.*$//g' log_for_health_check.txt
#sed 's/ *halt.*halt.*$//g' | sed 's/.*state=\(.*[0-9]\)/\1/' log_for_health_check.txt
cat log_for_health_check.txt | sed 's/ *halt.*$//g' | sed 's/.*state=\(.*[0-9]\)/\1/'  > stat_data.txt
python check_n_backup.py
