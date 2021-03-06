import os
import sys
import re
from shutil import copyfile

infile = sys.argv[1]
outfile = sys.argv[2]

remove_words = ['localhost','localhost.localdomain','local','broadcasthost','loopback','ip6-localnet','ip6-mcastprefix','ip6-allnodes','ip6-allrouters','ip6-allhosts','ip6-loopback',' CNAME rpz-passthru.']
    
with open(infile, 'r') as f:
    lines = f.read().splitlines()
with open(infile, 'w') as f:
    for line in lines:
        if not line.endswith((tuple(remove_words))):
            f.write('\n'.join([line + '\n']))

with open(infile) as f:
    file = f.read().split('\n')
    for i in range(len(file)):
        file[i] = re.sub('0\.0\.0\.0 0\.0\.0\.0\Z', '' ,file[i])
        file[i] = re.sub('\A127\.0\.0\.1 ', '', file[i])
        file[i] = re.sub('\A0\.0\.0\.0 ', '', file[i])
        file[i] = re.sub('\A0 ', '', file[i])
        file[i] = re.sub('\A:: ', '', file[i])
        file[i] = re.sub('\A::1 ', '' ,file[i])
        file[i] = re.sub(r'#', ';', file[i])
with open(infile, 'w') as f1:
    f1.writelines(["%s\n" % item  for item in file])
f.close() 
            
with open(infile, 'r') as f: # load file 
 lines = f.read().splitlines() # read lines
with open(infile, 'w') as f: # load file in write mode
 for line in lines:
     if line.startswith(';'):
      f.write('\n'.join([line + '\n']))
     elif not line.strip():
      f.write('\n'.join([line + '\n']))
     elif line.startswith('-'):
      f.write('\n'.join([line + '\n']))
     elif not line.startswith(';') and not line.startswith('-') and line.strip() and not ';' in line:
      f.write('\n'.join([line + ' CNAME .\n'])) # add CNAME . if file does not start with ; 
     elif ';' in line and not line.startswith(';'):
      f.write('\n'.join([line + '\n']))
f.close()

with open(infile) as f:
    file = f.read().split('\n')
for i in range(len(file)):
    file[i] = re.sub('\s\s+', ' ', file[i])
#print(file)
with open(infile, 'w') as f1:
    f1.writelines(["%s\n" % item  for item in file])
f.close() 

with open(infile) as f:
    file = f.read().split('\n')
for i in range(len(file)):
    file[i] = re.sub('\s;', ' CNAME . ;', file[i])
#print(file)
with open(infile, 'w') as f1:
    f1.writelines(["%s\n" % item  for item in file])
f.close()

copyfile(infile, outfile) # copy input file to output file
os.remove(infile) # remove input file

exit()