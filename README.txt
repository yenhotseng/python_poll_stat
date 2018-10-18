README

* Enable crontab as the below command for every 5 minutes check

cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*/5 * * * * root  /root/backup.sh
#

root@JBE10001059:~# df -H
Filesystem      Size  Used Avail Use% Mounted on
udev             11M     0   11M   0% /dev
tmpfs           104M   13M   91M  13% /run
/dev/mmcblk1p2  1.8G  1.6G  108M  94% /
tmpfs           259M     0  259M   0% /dev/shm
tmpfs           5.3M  4.1k  5.3M   1% /run/lock
tmpfs           259M     0  259M   0% /sys/fs/cgroup
tmpfs           259M  320k  258M   1% /tmp
/dev/mmcblk1p4  129M  1.7M  118M   2% /data
/dev/mmcblk0     16G  369M   15G   3% /media/sdcard

Move logfile to /tmp folder.


* Deploy 
Use the below command to run and measure the execution time --
# time source backup.sh

The execution time must be shorter than 5 minutes or the test will be failed.
--> Low the backup.sh sampling freq to 45000 for JBE10001306 target.

Then add the script to /etc/crontab as the above setting.
