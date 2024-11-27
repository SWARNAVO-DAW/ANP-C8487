#Question 5 
#If the ages of Ram, Sulabh and Ajay are input by the user, write a program to determine the youngest of the three.

age_ram = int(input("Enter Ram's age: "))
age_sulabh = int(input("Enter sulabh age: "))
age_ajay = int(input("Enter ajay age: "))

if age_ram < age_sulabh and age_ram < age_ajay:
    print("Ram is the youngest.")
elif age_sulabh < age_ram and age_sulabh < age_ajay:
    print("Sulabh is the youngest.")
elif age_ajay < age_ram and age_ajay < age_sulabh:
    print("Ajay is the youngest.")
else:
    print("Two or more have the same youngest age.")
