import random as r

def oddeven(x,y):
    z=x+y
    if z%2==0:
        return "EVEN"
    else:
        return "ODD"

opt1={"E":"EVEN","O":"ODD"}
opt2={"BAT":"BATTING","BALL":"BOWLING"}

print("Let's Play Hand Cricket 🏏\n")

while True:
    user=input("Choose Odd or Even [O,E] = ").upper()
    if user not in list(opt1):
        print("Invalid Input")
        continue
    else: break 

while True:
    try:
        usernum=int(input("Choose a number from 0-6 = "))
        if usernum not in range(0,7):
            print("Invalid Input")
            continue
        else:break 
    except ValueError:
        print("Enter a valid Integer")
    else: break

comp=r.randint(1,6)
print(f"Computer chose = {comp}\n")

result=oddeven(usernum,comp)
print(f"It's an {result} 👏")


if opt1[user]==result:
    print("You won the Toss 🎉")
    while True :
        usergame=input("Choose Batting or Bowling [bat,ball] = ").upper()
        if usergame not in list(opt2):
            print("Invalid Input")
            continue
        else: break

else:
    print("Computer won the Toss 🎉")
    compgame=r.choice(list(opt2))
    print(f"Computer chose = {compgame} !")
    if compgame=="BAT":
        usergame="BALL"
    elif compgame=="BALL":
        usergame="BAT"

class Game :

    def userbat(self):
        self.urun=0
        while True:
        
            print("\nIt's your Batting 🏏")
            compball=r.randint(0,6)
            while True :
                try:
                    userrun=int(input("Run = "))
                    if userrun not in range(0,7):
                        print("Choose from 0-6 !!")
                        continue
                    else: break
                except ValueError:
                    print("Enter a valid integer")
                else: break

            print(f"Ball = {compball}")

            if userrun==compball:
                print("\nWICKET 💔")
                break
            else:
                self.urun+=userrun

    def compbat(self):
        self.crun=0
        while True :
        
            print("\nIt's your Bowling ⚾")
            comprun=r.randint(0,6)
            while True :
                try:
                    userball=int(input("Ball = "))
                    if userball not in range(0,7):
                        print("Choose from 0-6 !!")
                        continue
                    else: break
                except ValueError:
                    print("Enter a valid integer")
                else: break

            print(f"Run = {comprun}")

            if userball==comprun:
                print("\nWICKET 💔")
                break
            else:
                self.crun+=comprun

g=Game()
if opt2[usergame]=="BATTING":
    g.userbat()
    g.compbat()
elif opt2[usergame]=="BOWLING":
    g.compbat()
    g.userbat()

print("\nFINAL SCORE :\n")
print(f"YOUR RUN = {g.urun}")
print(f"COMPUTER RUN = {g.crun}")

if g.urun>g.crun:
    print("\nThe Winner is YOU 🎉🎊")
elif g.urun<g.crun:
    print("\nThe Winner is COMPUTER 🥀😞")
else :
    print("It's a Tie 🤯")