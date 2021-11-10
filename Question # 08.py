# =============================================================================
# Write a python code that shows table of number using range function by using 
# loop.
# =============================================================================


num = int(input("\nEnter the Number whose Table you want to be displayed:"))
print("\n")
# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print("{}{}{}{}{}".format(num, ' X ', i, ' = ', num*i))