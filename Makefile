CC=gcc
Cflags=-c

main.o:
	$(CC) $(Cflags) main.c -o main.o

foo: main.o
	@echo "working"
	$(CC) main.o -o hello

clean:
	rm -rf *.o
