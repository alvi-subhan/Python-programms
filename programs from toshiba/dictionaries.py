di=dict()
inp=raw_input('enter text line')
print inp
sp=inp.split()
for text in sp:
    if text not in di:
        di[text]=1
    else:
        di[text]=di[text]+1
print di


