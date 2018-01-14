fh=open('subhan.txt')
string=''
di=dict()
for line in fh:
    string +=line
    su=string.split()
for name in su:
    if name not in di:
        di[name]=1
    else:
       di[name]=di[name]+1

c=di.keys()
print c
print len(c)
