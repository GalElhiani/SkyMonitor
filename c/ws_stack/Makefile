CC = gcc
CFLAGS = -ansi -pedantic-errors -Wall -Wextra -DNDEBUG -O3
OBJS = stack.o main.o

result: $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o result


%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

stack.o: stack.h

clean:
	rm *.o result