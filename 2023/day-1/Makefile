CC = gcc
CFLAGS = -Wall

SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)

TARGET = main

all: run clean 

$(TARGET): $(OBJ)
	@$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	@$(CC) $(CFLAGS) -c -o $@ $<

run: $(TARGET)
	@./$(TARGET)
clean:
	@rm -f $(OBJ) $(TARGET)
