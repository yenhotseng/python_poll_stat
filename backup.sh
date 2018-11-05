#!/bin/bash

if [ -a /tmp/stat_data.txt ]
then rm /tmp/stat_data.txt
  echo removed stat log file
fi

if [ -a /tmp/log_for_health_check.txt ]
then rm /tmp/log_for_health_check.txt
  echo removed old log file
fi

echo sampling......

/root/read_f 270
cat /tmp/log_for_health_check.txt | sed 's/ *halt.*$//g' | sed 's/.*state=\(.*[0-9]\)/\1/'  > /tmp/stat_data.txt

cat /tmp/log_for_health_check.txt | grep 'halt=1,1'  > /tmp/halt.txt

python check_n_backup.py

if [ -a /tmp/halt.txt ]
then rm /tmp/halt.txt
  echo removed halt log file
fi
