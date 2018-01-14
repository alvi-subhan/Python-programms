from random import randint
lis=[]
while len(lis)!=3:
    gen=randint(2,4)
    inp=int(input("make a guess "))
    if gen==inp:
            print ("You won ")
            #asking to play again
            del lis[:]
            ask=input("Do you want to play again? Type yes or no ")
            if ask=="Yes" or ask =="YES" or ask=="yes" :
                lis.append(ask)
            else:
                print ("See you next time")
                break
    else:
            print ("Print you loose")
            lis.append(gen)
print (lis)
            
