x=input("type anything ")
lis=[]
for c in x:
    lis.append(c)
lis=lis[::2]
#merging the items in list
merg=[''.join(lis[:])]
print (merg[0])
