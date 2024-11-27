#Question 1 :
#Any integer is input by the user. Write a program to find out whether it is an odd number or even number. 

number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"The number {number} is Even.")
else:
    print(f"The number {number} is Odd.")