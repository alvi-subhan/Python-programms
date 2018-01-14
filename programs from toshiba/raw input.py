counts=dict()
y=open('mbox-short.txt')
for line in y:
    if line.startswith('From '):
        x=line.split()
        y=x[1]
for names in y:
    counts[names]=counts.get(names,0)+1
print counts
