x=open('xyzrandom.txt')
string=''
xyz=9
while xyz>0:
    for line in x:
        if line.startswith('xyz'):
            y=line
            for num in y:
                string+=num
                su=string.split()
    print len(su)
    xyz=xyz-1
