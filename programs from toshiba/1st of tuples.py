fhand=open('mbox-short.txt')
counts=dict()
string=''
ls=list()
for fg in fhand:
    if fg.startswith ('From '):
        w=fg.split()
        x=w[1]
        for line in x:
            string+=line
            sp=string
            
ls.append(sp)

print ls

print len(ls)


lisk=['3','5','34']
print len(lisk)
print len(lisk)+len(ls)
