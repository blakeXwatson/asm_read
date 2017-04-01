;;THIS FILE READS TEMP.LSP, A LISP-FRIENDLY FORMAT FOR THE OBJDUMP
;;AND ENACTS THE SECOND PASS IN THE DISASSEMBLY

;;(DEFVAR IN_LIST Nil)
;;(DEFVAR IN (OPEN "temp.lsp" :IF-DOES-NOT-EXIST Nil) )
  
(defvar in (open "temp.lsp"))
(defvar lines (list " " " "))
(when in
    (loop for line = (read-line in nil)
         while line do (append lines 'line))
    (close in))

(list lines)

(DEFUN A_PRINT (ARG) (FORMAT T "~A~%" ARG ))


(DEFUN A_SECTION (SECTION_NAME)
  "TEMPORARY CODE.  WILL MAKE COOLER LATER."
  (PUSH IN_LIST SECTION_NAME))


(DEFUN A_METHOD (METHOD_NAME)
  "TEMPORARY CODE.  ETC..."
  (PUSH A_LIST METHOD_NAME))

(DEFUN A_ADDRESS (ADDR)
  "TEMP"
  (PUSH A_LIST ADDR))

(DEFUN A_CODE (INSTR)
  "TEMP"
  (PUSH A_LIST INSTR))

;;(DOLIST IN_LIST 
;;  (EACH (PRINT (WRITE-TO-STRING EACH)  )))

    
