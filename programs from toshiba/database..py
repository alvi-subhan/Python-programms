fh=open('mbox-short.txt')
d=dict()

for line in fh:
    if line.startswith('From '):
        piece=line.split('@')
        x=piece[1]
        y=x.split()
        sp=y[0]
        print sp

