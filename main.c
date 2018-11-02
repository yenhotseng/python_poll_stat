#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	char buf[1024] = {0x0};
	FILE *wd;
	FILE *fd;
	int i, j;
	long runs = 0;


	if (argc == 2) {
		runs = atol(argv[1]);
		printf("%s\n", argv[1]);
		printf("%ld\n", runs);
	} else {
		printf("%s : add run sec counts\n", argv[0]);
		exit(1);
	}
	wd = fopen("/tmp/log_for_health_check.txt", "aw+");

	for (j = 0; j < runs; j++) {
		for (i = 0 ; i < 180 ; i++) { // 180 per sec
			fd = fopen("/sys/bus/iio/devices/iio:device0/sampling_frequency", "r");
			fgets(buf, 1024, fd);
			fputs(buf, wd);
			fclose(fd);
			usleep(5000);
		}
	}
	fclose(wd);
	return 0;
}
