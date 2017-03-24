import subprocess
import os

DISS=''
EXE=''

def set_exe(file):
  global EXE
  EXE = file


def file_exists():
  
  try:
    f=open(EXE, 'r')
    return True
  except IOError:
    return False

def get_diss():
  if file_exists():
    try:
      return subprocess.check_output(['cmd', '/c', 'objdump', '-d', EXE, '-Mintel'])
    except:
      return ''

def prompt_exe():
  while not file_exists():
    set_exe(raw_input('Enter path to executable: '))


prompt_exe()
DISS=get_diss().split('\n')    

################################################################
#Cool.  We now have the disass.  Next step=find stuff
#list vulnerable calls (strcmp, strcpy, malloc)

def find(call):  #takes strings and lists as arguments.  returns list of indices
  lines=[]
  isList=False
  if type(call) == type([1, 2, 3]):
    isList=True 
  if isList:
    for each in DISS:
      has_all=True
      for beach in call:
        if beach not in each:
          has_all=False
      if has_all:
        lines.append(DISS.index(each))
  else:
    for each in DISS:
      if call in each:
        lines.append(DISS.index(each))
  return lines


def print_search(call):  #prints search results
  print ''
  search_result=find(call)
  for each in range(0, len(search_result)):
    print DISS[search_result[each]]
  print ''

def search(cmd):
  #cmd=''
  #while cmd != 'quit'.split(' '):
    #if cmd!='':
  if ' ' in cmd:
    cmd=cmd.split(' ')
  print_search(cmd)
    #cmd = raw_input('enter search term/terms: ').split(' ')

def get_line(line):
  res=find(line+':')
  #for each in range(0, len(res)):
  if len(res)>0:
    return DISS[res[0]]
  else:
    return ''

def get_range(addr1, addr2):
  lines=[]
  try:
    addr1 = hex( int(addr1, 16) )
    addr2 = hex( int(addr2, 16) )
  except:
    print 'type mismatch'
    console()  
  
  for each in range(int(addr1, 16),int(addr2, 16)+1):
    #print get_line(hex(each).replace('0x',''))
    addr=str(hex(each).replace('0x', ''))
    #print addr
    lines.append(get_line(addr) )   
  return lines 


def find_next(start_addr, call):
  next=''
  res = find(call)
  start_index=DISS.index(get_line(start_addr))
  for each in res:
    if each>start_index:
      #next= DISS[each]
      #break
      return DISS[each]
      


def get_start():
  for each in DISS:
    if ':' and '>' and '<' in each:
      print each
      break

def get_end():
  for each in DISS[::-1]:
    if ':' in each:
      print each
      break 

  
def console():
  cmd=raw_input(EXE + '$ ')
  if cmd=='quit':
    exit()
  elif cmd =='calls':
    print_search('>:')
  elif 'line' in cmd:
    print get_line(cmd.split(' ')[1])
  elif cmd=='help':
    print 'line <num,hex>, search <arg/s>, show <addr1> <addr2>, next <start-addr> <search arg/s>, calls, start, end, clear, quit'
  elif cmd=='start':
    get_start()
  elif cmd=='end':
    get_end()
  elif cmd=='clear':
    os.system('cls')
  
  elif 'search' in cmd:
    search(cmd.replace('search ',''))
  
  elif 'show' in cmd:
    if len(cmd.split(' '))>2:
      for each in get_range(cmd.split(' ')[1], cmd.split(' ')[2]):
        if each !='':  
          print each
    else:
      print 'not enough arguments' 

  elif 'next' in cmd:
    if len(cmd.split(' '))>2:
      addr=cmd.split(' ')[1]
      next = find_next(addr, cmd.split(' ')[2:])
      print next
    else:
      print 'not enough arguments'
  elif cmd=='':
    1+1
  else:
    print 'Command not found: ' + cmd
  
  console()

console()


###############################################
"""

Notes

map control flow:  #probably recursive
  find the next jump or call after the entry point
    find the next jump or call from that address
      etc...
      each ret pops back to the call before

  
identify conditionals and loops:
  easier once control flow is mapped


identify data structures


fingerprint popular compilers?


allow for address/name resolution in commandline syntax (ie... "line <__strcpy__>" )



step forward/back addresses


"""
###############################################









