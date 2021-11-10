# =============================================================================
# Write a program to display all the prime numbers within a range using loop.
# =============================================================================

#taking starting index as input
starting_index=int(input("enter starting range:"))

#taking ending index as input
ending_index=int(input("enter ending range:"))

#using nested loop for the calculation
for num in range(starting_index, ending_index+1):
    if num > 1:
        for i in range(2,num):
           if ( num % i) == 0:
               break
        else:
              print("{}{}{}{}{}".format(num, " is also a Prime Number between ", starting_index, " & ", ending_index))