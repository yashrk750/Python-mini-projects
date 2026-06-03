def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("This is Your Calculator !\n")

x=int(input("Enter first number="))
y=int(input("Enter second number="))

dict={"a":add(x,y),"s":sub(x,y),"m":mul(x,y),"d":div(x,y)}

while True:
    choice=input("\nChoose :\nAdd -'a'\nsubtract -'s'\nMultiply -'m'\nDivide -'d'\n=").lower()
    if choice not in list(dict):
        print("Invalid Input !")
        continue
    else:
        break

for i in list(dict):
    if choice==i:
        print(f"\nAnswer = {dict[choice]}")