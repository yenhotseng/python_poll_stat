#!/bin/bash

if [ -a /tmp/stat_data.txt ]
then rm /tmp/stat_data.txt
  echo removed old log file
fi

if [ -a /tmp/log_for_health_check.txt ]
then rm /tmp/log_for_health_check.txt
  echo removed old log file
fi

echo sampling......

/root/read_f 270
cat /tmp/log_for_health_check.txt | sed 's/ *halt.*$//g' | sed 's/.*state=\(.*[0-9]\)/\1/'  > /tmp/stat_data.txt
python check_n_backup.py
