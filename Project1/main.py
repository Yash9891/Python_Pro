'''

-1 water
1 snake
0 gun
'''

import random
computer =random.choice([-1,0,1])
youstr=input("Enter your choise :")

youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr] 

if(computer==you):
    print("Its a draw")
else:
    if(computer==-1 and you==1):
        print("You win")
    elif(computer==-1 and you==0):
        print("You Lose")
    elif(computer==1 and you==-1):
        print("You Lose")
    elif(computer==1 and you==0):
        print("You Lose")
    elif(computer==0 and you==-1):
        print("You Win")
    elif(computer==0 and you==1):
        print("You Lose")
    else:
        print("Something went wrong")