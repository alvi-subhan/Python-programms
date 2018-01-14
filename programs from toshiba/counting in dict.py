fh=open('subhan.txt')
string=''
di=dict()
for line in fh:
    string +=line
    list=string.split()
for name in list:
    if name not in di:
        di[name]=1
    else:
        di[name]=di[name]+1
print di
#for len of dict;
print len(di)

print list[2:3]
