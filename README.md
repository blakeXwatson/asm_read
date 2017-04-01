This branch includes an updated python hex parser, which read assembly in and saves it into a Lisp formatted list.  The Lisp file, process.lsp, is the first in a series of attempts at taking advantage of Lisp's data structure.  
pass_two.py is responsible for more advanced parsing;  this will be the file the operates upon temp.lsp and updates is with Lisp tags, such that the structure of the file will eventually contain all of the pieces necessary to run as fully functional Lisp language, which uses pieces of asm, ROP gadgets, as interchangeable bits of both assembly and CLisp.  Compiler theory is in progress.
