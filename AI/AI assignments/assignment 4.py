inp=input("Enter ")
lis=[]
dic={}
for x in inp:
    lis.append(x)
print (lis)
for item in lis:
    if item not in dic:
        dic[item]=1
    else:
        dic[item]+=1
#the below syntax will delete the blank spaces from         
if " " in dic:
    del dic[" "]
for key,value in sorted(dic.items()):
    print (key+"," + str(value))
