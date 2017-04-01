#format ->
#addr, then the code on that line
#code
#call, ret
#hints: 
  #a comma always precedes the second arg to an instruction

def code_at_address(address):   #gives the code at the given address.  
  address=address.replace('"', '')
  if ')' in address:
    return 'register'
  for each in lines:

    if line_type(each)=='address':
      
      listed_addr = each.split('"')[1]  #the addr found at each
      #print each + ' : ' + address + ' : ' + listed_addr
      if listed_addr==address:
        try:
          return lines[lines.index(each)+1]
        except:
          return 'address_out_of_range'
  return 'address_not_found'


def get_operands(line):
  parts=line.split(' ')
  return parts[1:]
  

def print_list(list):
  for each in list: print each


def line_type(line):
  line=line.split(' ')
  #print '\n'+str(line[0])
  if '(a_' in line[0]:
    return line[0].split('_')[1]
  else:
    return 'error determining line type of line:  ' + line[0]

def instr_type(line):
  data = line.split('\"')[1].split('\"')[0]
  parts=data.split(' ')
  instr=parts[0].replace(',', '')  #remove any trailing commas

  c_jumps=['jo', 'jno', 'js', 'jns', 'je', 'jz', 'jne', 'jnz',
  'jb', 'jnae', 'jc', 'jnb', 'jae', 'jnc', 'jbe', 'jna', 'ja',
  'jnbe', 'jl', 'jnge', 'jge', 'jnl', 'jle', 'jng', 'jg', 'jnle',
  'jp', 'jpe', 'jnp', 'jpo', 'jcxz', 'jecxz']

  common = ['jmp', 'call', 'ret', 'mov', 'lea']
  stack= ['push', 'pop']
  
  if instr in c_jumps:
    return 'c_jump'
  elif instr in common:
    return instr
  elif instr in stack:
    return 'stack'
  else:
    return 'arithmetic'
  

def next_ret(start_address):  
  #start_address=start_address.replace('"', '')
  start_index=0
  for each in lines:
    #print each.split(' ')[1].replace(')', '')
    if line_type(each)=='address' and each.split(' ')[1][1:-2]==start_address:
      start_index=lines.index(each)
      break
  print start_index
  ind=start_index
  for each in lines[start_index:]:
    print '     --->    ' + each
    if line_type(each)=='code' and instr_type(each)=='ret':
      return ind
    ind=ind+1
  return '0'   #0 is error
  #after this, just iterate until you hit a ret
  

f=open('temp.lsp', 'r+')
fin=''
for each in f.read():
  if len(each)>0:   #helps prevent odd errors from blanks and shit
    fin = fin + each
lines=fin.split('\n')


for each in lines:#[:50]:
  if line_type(each)=='code':
    print each + '  ->  type: ' + instr_type(each)
    print 'code, linetype = ' +line_type(each)
    if instr_type(each)=='call':
      address=each.split(' ')[2].strip()      
      end_index= next_ret(address)
      print '  start: ' + address + '  code  ->  ' + code_at_address(address) 
      print '  end  : ' + lines[end_index-1] + '  code  ->  ' + lines[end_index]+'\n'  
  
  else:
    print each# + '  ' + line_type(each) 
  
