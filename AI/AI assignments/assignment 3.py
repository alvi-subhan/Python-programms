inp=input("Type anything to get in reverse order ")
lis=[]
for x in inp:
    lis.append(x)
lis=lis[::-1]
merge =[''.join(lis[:])]
print (merge)
