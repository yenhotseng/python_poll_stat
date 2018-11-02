#include <stdio.h>
#include <stdlib.h>

char run_cmd[] = "cat /sys/bus/iio/devices/iio\\:device0/sampling_frequency >> /tmp/log_for_health_check.txt";

int main(int argc, char *argv[])
{
   long runs = 0;

   printf("argc : %d\n", argc);
   if (argc == 2) {
     runs = atol(argv[1]); 
     printf("%s\n", argv[1]);
     printf("%d\n", runs);
   }

  for ( int i = 0; i < runs; i++) {
    // system("cat /sys/bus/iio/devices/iio\:device0/sampling_frequency >> /tmp/log_for_health_check.txt");
    system(run_cmd);
  }

   return 0;
}

