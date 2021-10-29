import math
import datetime
# stores first name in lowercase and last name in upper case into variables,
firstName = input("Enter First name:").lower();
lastName = input("Enter Last name:").upper();
#Prints out, "Hello, First and last name with the first name converted to uppercase letters and the last name converted to lowercase
print("Hello ", firstName.upper(), lastName.lower());
#Prints out two newlines
print("\n\n");
#Creates a new variable that stores your first and last name together with a space between both parts. 
fullName = firstName + " " + lastName;
print(fullName);
#Slices your last name from the variable.  
print(fullName.split(" ")[1]);
#Replaces  last name in the variable by adding string
nameWithCollege = fullName.split(" ")[1] + ",Walsh College Student"
#print previusly declared variable
print(nameWithCollege);
#print statement with double quote
print("\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\"");
#declared two decimal variables
decNumber1 = 40.23;
decNumber2 = 32.12;
# stored Addition, substraction , Multiplication & division into variables
addition = decNumber1 + decNumber2;
substractionVal = decNumber1 - decNumber2;
mulVal = decNumber1 * decNumber2;
divVal = decNumber1/decNumber2;
#print results with string format.
print(f"{decNumber1:.2f} plus {decNumber2:.2f} equals {addition:.2f}");
print(f"{decNumber1:.2f} minus {decNumber2:.2f} equals {substractionVal:.2f}");
print(f"{decNumber1:.2f} multiply {decNumber2:.2f} equals {mulVal:.2f}");
print(f"{decNumber1:.2f} division {decNumber2:.2f} equals {divVal:.2f}");
#store srqt into variable
sq_root = math.sqrt(mulVal);
#print the result
print(f"The square root of {mulVal:.2f}  equals {sq_root:.2f}");
#store current month as string into variable
monthName = datetime.datetime.now().strftime(("%B"));
day = datetime.datetime.today().day
# print day and month with tabs and new line
print(f"Today is day\t\t {day}\nof the month of\t\t{monthName}");

