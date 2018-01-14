counts=dict()
y=open('subhan.txt')
string=''
for line in y:
    string +=line
    sp=string.split()
    if line.startswith('From '):
        print sp

