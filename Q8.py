#Question 8 
#In a company an employee is paid as under: 
#If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary 
#and DA = 90% of basic salary.
#If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 
#and DA = 98% of basic salary. 
#If the employee's salary is input by the user write a program to find his gross salary. 

basic_salary = float(input("Enter the basic salary of the employee: "))

if basic_salary < 1500:
    hra = 0.10 * basic_salary  # HRA is 10% of basic salary
    da = 0.90 * basic_salary  # DA is 90% of basic salary
else:
    hra = 500  # Fixed HRA
    da = 0.98 * basic_salary  # DA is 98% of basic salary

gross_salary = basic_salary + hra + da

print(f"The gross salary of the employee is Rs. {gross_salary:.2f}")