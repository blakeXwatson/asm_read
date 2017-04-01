import sys
from subprocess import call
pass_one=[]

def parse(line):
  global pass_one

  if each=='' or each=='\n':  #sloppy.
    1+1

  elif 'section .' in each:  #section
    section=each.split('section ')[1][:-1]
    pass_one.append( '(a_section \"' + section + '\" )' )

  elif each[0]=='0':
    method_name = each.split(' ')[1][:-1]
    pass_one.append( '(a_method \"' + method_name + '\")' )
    

  elif each[0:2]=='  ':
    address=each.split(':')[0][2:]
    #get code
    code=each[32:]

    while '  ' in code:  #format code
      code=code.replace('  ', ' ')

    pass_one.append( '(a_address \"' + address + '\")' )
    pass_one.append( '(a_code \"' + code.strip() + '\")' )

FILENAME=''
if sys.argv >= 1:
  try:
    FILENAME=sys.argv[1]
  except:
    print 'You must pass a filename'

try:
  f=open(FILENAME, 'r')
  f.close()
except:
  print 'File not found'
  exit()
call(['cmd', '/c', 'objdump', '-D', FILENAME, '-Mintel', '>', 'temp.txt'])
try:
  f=open('temp.txt', 'r')
except:
  print 'Error getting disassembly'
  exit()


input=''
for each in f.read():
  input=input+each
f.close()
lines=input.split('\n')

for each in lines:
  parse(each)

try:
  f=open('temp.lsp', 'w')
except:
  print 'Error writing to file'

for each in pass_one:
  each=each.replace(',', ', ')
  f.write(each+'\n')

