n=int(input("enter any number "))
x=1
y=2
lis=[]
while n>=x:
#fr = fraction
    fr=(n+x-n)/(n+y-n)
    x+=1
    y+=1
    lis.append(fr)
for val in lis:
    val+=val
print (val)
