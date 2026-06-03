import random as r

num=r.randint(1,50)
while True:
    n=int(input("Guess a number between 1 to 50 ="))  
    if(n>num):
        print("Too High !")
    elif(n<num):  
        print("Too Low !")
    elif(n==num): 
        print("You guessed the Number !")
        break
print("You have Won !")