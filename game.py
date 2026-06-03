import random as r

main={"r":"🪨","p":"📃","s":"✂️"}
win=0
lose=0

while True:
    comp=r.choice(list(main))

    while True:
        user=input("Choose Rock Paper Scissor [r,p,s]=").lower()
        if user not in list(main):
            print("Invalid input")
            continue
        else:
            break

    print(f"You chose {main[user]}  and Computer chose {main[comp]}\n")

    if(user=="r"and comp=="s")or(user=="p"and comp=="r")or(user=="s"and comp=="p"):
        print("You have Won 🎉\n")
        win+=1
    elif(user==comp):
        print("It's a Tie 🤝\n")
    else:
        print("You have Lost 😢\n")
        lose+=1

    while True :
        choice=input("Do you want to continue [y,n]=").lower()
        if choice not in ["y","n"]:
            print("Invalid input")
            continue
        else:
            break
        
    if(choice=="n"):
        break

print(f"\nYour Score :\nWin ={win}\nLose ={lose}")
print("Thanks for Playing !")