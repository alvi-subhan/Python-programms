numlist=list()
while True:
    inp=raw_input('enter :')
    if inp=='done': break
    f=float(inp)
    numlist.append(f)
average=sum(numlist)/len(numlist)
print average
