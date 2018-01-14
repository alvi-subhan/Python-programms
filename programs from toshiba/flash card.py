import random
re=open('states.txt')
string=''

for line in re:
    string+=line
    sp=string.split()
parse=(random.choice(sp))
spli=parse.split(',')
print spli[0]
x=spli[1]
ques=raw_input('enter the captial')
if ques==x:
    print 'very good '+'u did it right'
else:
    print 'the correct answer is ' + spli[1]
