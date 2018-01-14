#this code will take the input and will show the odd letters/number of input
x=input("type anything ")
print("subhan")
lis=[]
for c in x:
    lis.append(c)
lis=lis[::2]
#merging the items in list
merg=[''.join(lis[:])]
print (merg[0])
