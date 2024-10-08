#Eng. Mohamed Gamal
CC=gcc
CFLAGS=-w -Werror -Wall
Deg=-g
INCS=-I .
LIBS=
SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)
As = $(wildcard *.s)
AsOBJ = $(As:.s=.o)
File=Output


all: $(File) 
%.o: %.c
	$(CC).exe -c $(Deg) $(INCS) $(CFLAGS) $< -o $@ 
 
 
$(File): $(OBJ) $(AsOBJ)
	$(CC) $(LIBS) $< -o $@ 
	@echo '============Bulid_Done============' 


debug: $(File).elf
	$(CC)strip.exe -g -S -d $<
	@echo '============rm_degig_Done============' 
 

clean:
	rm *.o *.exe
	@echo @echo '============rm_all============' 
 