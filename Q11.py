#Question 11
#Any character is entered by the user; write a program to determine whether the character entered is a capital letter, a small case letter, a digit or a special symbol. The following table shows the range of ASCII values for various characters. 
#Characters 
#ASCII Values 
#A – Z 	65 – 90
#a – z 	97 – 122


char = input("Enter a character: ")

if 'A' <= char <= 'Z':  # Check if it's a capital letter
    print("The character is a capital letter.")
elif 'a' <= char <= 'z':  # Check if it's a small letter
    print("The character is a small letter.")
elif '0' <= char <= '9':  # Check if it's a digit
    print("The character is a digit.")
else:  
    print("The character is a special symbol.")