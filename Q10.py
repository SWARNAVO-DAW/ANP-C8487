#Question 10
#The marks obtained by a student in 5 different subjects are input by the user. The student gets a division as per the following rules:
#Percentage above or equal to 60 - First division 
#Percentage between 50 and 59 - Second division 
#Percentage between 40 and 49 - Third division 
#Percentage less than 40 - Fail 
#Write a program to calculate the division obtained by the student. 

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter the marks for subject {i}: "))
    marks.append(mark)

total_marks = sum(marks)
percentage = (total_marks / 500) * 100  # Assuming each subject has a maximum of 100 marks

if percentage >= 60:
    division = "First Division"
elif 50 <= percentage < 60:
    division = "Second Division"
elif 40 <= percentage < 50:
    division = "Third Division"
else:
    division = "Fail"

print(f"Total Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Division: {division}")