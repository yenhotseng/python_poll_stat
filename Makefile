CC:=gcc
exe:=read_f
obj:=main.o 

all:$(obj)
	$(CC) -o $(exe) $(obj)

%.o:%.c
	$(CC) -c $^ -o $@

.PHONY:clean
clean:
	rm -rf $(obj) $(exe)
