cube=27
guess=0
eps=0.001
inc=0.0001
numofg=0
while abs(guess**3-cube) >= eps :
    guess+=inc
    numofg+=1
print (numofg)
print(guess)
 
