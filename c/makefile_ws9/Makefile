CC = gcc
CFLAGS = -ansi -pedantic-errors -Wall -Wextra -DNDEBUG -O3
OBJS = foo.o foo_test.o

result: $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o result


%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

foo.o: foo.h

clean:
	rm *.o result