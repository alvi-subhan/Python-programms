handle=open('subhan.txt','r')
text=handle.read()
words=text.split()
count=dict()
for word in words:
    count[word]=count.get(word,0)+1
bcount=None
bword=None
for word,count in count.items():
    if bcount == None or count>bcount:
        bword=word
        bcount=count
print bword,bcount
print len(text)
