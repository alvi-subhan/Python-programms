lis=["2","3","6","4","12","19"]
ask=int(input("how many numbers do you want in your list "))
#matching the input with length of lis
while len(lis) != ask:
    inp=input("enter the number")
    if inp not in lis:
        lis.append(inp)
    else:
        print (inp + " is already in the list")

print ("here is the list without any repeated numbers " )
print (lis)
