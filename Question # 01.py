# =============================================================================
# Write a program to swap the values of two integer variables without using a 
# third variable.
# =============================================================================

#initializing two variables
num1 = 12
num2 = 24

print("\nValues Before swapping: ")
print("{}{}".format("NUM1 = ", num1))
print("{}{}".format("NUM2 = ", num2))

#logic to swap
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

#Printing the values after swapping
print("\nValues After swapping: ")
print("{}{}".format("NUM1 = ", num1))
print("{}{}".format("NUM2 = ", num2))