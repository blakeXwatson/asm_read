# asm_read
Beta version 1
executable static analysis tool

written for python 2.7 on windows

Parses and analyses objdump output.  Allows navigation of the exe, searches for lines containing one or more expressions, line display, identifies start and end of hex, finds next instance of an expression, lists libraries called, and displays a given address range.

I'll be putting control flow mapping in here next update.


Please report any issues you find

Uses Objdump, from MinGW.  You can get that here:  
https://sourceforge.net/projects/mingw/files/MinGW/Base/binutils/binutils-2.22/binutils-2.22-1-mingw32-bin.tar.lzma/download


Once you have MinGW you must also make sure that objdump is included in the path.



################################################################################################
                                              Commands
                                              
line <addr>                 #display line at the given address 
search <arg/s>              #display all lines containing the given argument or arguments
show <addr1> <addr2>        #displays all addresses in the given range.
next <start-addr> <arg/s>   #takes a starting address and displays the next line containing the given argument or arguments.
calls                       #list function calls
start                       #show start address
end                         #show end address
clear                       #clear screen
quit                        #quit



