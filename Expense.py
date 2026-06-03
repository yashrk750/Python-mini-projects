bill={}

print("Make Your Expense Chart !")
while True:
    exp=input("\nEnter your Expenditure = ")

    if (exp=="Done" or exp=="done"):
        break
    while True:
        try:                                            #EXCEPTION HANDLING
            amt=int(input(f"Enter {exp} Amount = "))
        except ValueError:
            print("Enter a valid Integer !!")
        else:
             break

    bill[exp]=amt                                  #UPDATE DICT

print("This is your Expense Chart !\n")
for i in list(bill):
    print(f"{i} - {bill[i]}")

total=sum(bill.values())
print(f"Your total Expense is = {total}")