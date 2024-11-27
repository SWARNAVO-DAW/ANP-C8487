#Question 3 
#Write a program to calculate the total expenses. Quantity and price per item are input by the user and discount of 10% is offered if the expense is more than 5000. 

quantity = int(input("Enter the quantity of items: "))
price_per_item = float(input("Enter the price per item: "))
total_expense = quantity * price_per_item

if total_expense > 5000:
    discount = total_expense * 0.10 
    total_expense -= discount
    print(f"A discount of 10% has been applied. Discount amount: {discount:.2f}")
print(f"The total expense is: {total_expense:.2f}")