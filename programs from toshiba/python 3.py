fh=open('mbox-short.txt')
random=dict()
string=''
for line in fh:
    if line.startswith("From "):
        x=line.split()
        y=x
        print (y)
