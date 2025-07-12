import random
'''
1 for snake 
-1 for water
0 for gun
'''
computer = random.choice([1,-1,0])
yourchoise = input ("Enter your choise :")
youdict = { "s" : 1 , "w" : -1 , "g" : 0}
reversedict = { 1 : "s" ,  -1 : "w" , 0 : "g"}

you = youdict[yourchoise]
 
print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if (computer == you):
    print("it's a draw")
else:
    if(computer == 1 and you == -1):
        print(" you lose!") 
    elif(computer == 1 and you == 0):
        print(" you win!") 
    elif(computer == -1 and you == 1):
        print(" you win!") 
    elif(computer == -1 and you == 0):
        print(" you lose!") 
    elif(computer == 0 and you ==  1):
        print(" you lose!") 
    elif(computer == 0 and you == -1):
        print(" you win!") 
    else:
        print("something went wrong")