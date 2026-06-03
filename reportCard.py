def grade(x):
    if x>=90 and x<=100:
        return "A"
    elif x>=80 and x<90:
        return "B"
    elif x>=70 and x<80:
        return "C"
    elif x>=60 and x<70:
        return "D"
    elif x>=40 and x<60:
        return "B"
    else :
        return "F"

student={}

for i in range(0,5):
    sub=input(f"\nEnter {i+1} Subject name = ")

    while True:                                              # DOUBLE ERROR HANDLING
        try:
            marks=int(input(f"Enter {sub} Marks = "))
            if marks not in range(0,101):
                print("Enter valid number between 1-100 !") 
                continue
            else:
                break
        except ValueError:
            print("Enter a valid Integer")
        else:break

    student[sub]=marks

print("\nHere is your REPORT CARD :")

for n in list(student):
    print(f"{n} - {student[n]} - {grade(student[n])}")

per=sum(student.values())/5
print(f"\nPercentage = {per}%")