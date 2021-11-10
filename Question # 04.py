# =============================================================================
# Write a program that asks the user to enter an operand (such as +, -, *, /) 
# and two integers. Perform the operation on the integers depending on the 
# operands.
# =============================================================================

#Taking inputs
operand = input("\nEnter one of the arithematic operand(+,-,*,/) : ")
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter another Number: "))

#using conditionals to perform the respective arithatic ooperation
if operand == "+":
    print("\n{}{}{}{}{}{}".format("Sum of ", num1, " & ", num2, " is: ", num1 + num2))
    
elif operand == "-":
    print("\n{}{}{}{}{}{}".format("Difference of ", num1, " & ", num2, " is: ", num1 - num2))
    
elif operand == "/":
    print("\n{}{}{}{}{}{}".format("Product of ", num1, " & ", num2, " is: ", num1 * num2))
    
elif operand == "+":
    print("\n{}{}{}{}{}{}".format("Division of ", num1, " & ", num2, " is: ", num1 / num2))
    
else:
    print("You have entered an invalid input! Please try again.")