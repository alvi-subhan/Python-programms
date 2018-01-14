import re
handle = raw_input("Enter file name: ")
fh = open(handle)
for line in fh:
    line=line.rstrip()
    if re.search('^From:',line):
        print line
