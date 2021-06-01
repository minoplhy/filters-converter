import os
import sys
from re import sub
from shutil import copyfile

infile = sys.argv[1]
outfile = sys.argv[2]

a = ['address=/','/#','server=/','/','127.0.0.1','0.0.0.0','::1']
lst = []

with open(infile, 'r') as f:
 for line in f:
    for word in a:
        if word in line:
             line = line.replace(word,'')
    lst.append(line)
f.close()
with open(infile, 'w') as f:
 for line in lst:
    f.write(line)
f.close()

with open(infile) as f:
    file = f.read().split('\n')
for i in range(len(file)):
    file[i] = sub(r'#', ';', file[i])
#print(file)
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
  elif line.endswith('1.1.1.1') or line.endswith('2606:4700:4700::1111'):
   f.write('\n'.join([line + '\n']))
  elif not line.startswith(';') and line.strip() and not line.endswith('1.1.1.1') and not line.endswith('2606:4700:4700::1111'):
   f.write('\n'.join([line + ' CNAME .\n'])) # add CNAME . if file does not start with ; 
f.close()


with open(infile) as f:
    file = f.read().split('\n')
for i in range(len(file)):
    file[i] = sub('1.1.1.1$', '', file[i])
#print(file)
with open(infile, 'w') as f1:
    f1.writelines(["%s\n" % item  for item in file])
f.close()

with open(infile) as f:
    file = f.read().split('\n')
for i in range(len(file)):
    file[i] = sub('2606:4700:4700::1111$', '', file[i])
#print(file)
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
  elif line.endswith('CNAME .'):
   f.write('\n'.join([line + '\n']))
  elif not line.endswith('CNAME .') and line.strip():
   f.write('\n'.join([line + ' CNAME rpz-passthru.\n']))

copyfile(infile, outfile) # copy input file to output file
os.remove(infile) # remove input file

exit()