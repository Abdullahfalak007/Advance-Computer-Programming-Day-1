# =============================================================================
# Write a program that asks the user to type 10 integers and write the smallest 
# value.
# =============================================================================

#taking comma seperated integers in the list
mylist = list(map(int,input("Enter array elements at once and split them by comma:").split(",")))

#Assuming the first number to be the smallest Number
min_num =mylist[0]

#usinf for loop to itterate through the list and find the smallest Number
for i in range(1,len(mylist)):
    if(mylist[i] < min_num):
        min_num = mylist[i]
        
#Printing the smallest number onto the console Window
print("{}{}".format("\nSmallest Number is: ", min_num))
