# =============================================================================
# From the two list, make a new list, containing only numbers which are 
# divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
# =============================================================================

#taking inputs in two seperate lists
list1 = list(map(int,input("Enter array elements at once and split them by comma:").split(",")))
list2 = list(map(int,input("Enter array elements at once and split them by comma:").split(",")))

#declaring list for each number
four_list = []
six_list = []
eight_list = []
ten_list = []
three_list = []
five_list = []
seven_list = []
nine_list = []

#using for loop to append the third list
for i in list1:
    if i%4 == 0:
        four_list.append(i)
    
    elif  i%6 == 0:
        six_list.append(i)
        
    elif  i%8 == 0:
        eight_list.append(i)
        
    elif  i%10 == 0:
        ten_list.append(i)
        
    elif  i%3 == 0:
        three_list.append(i)
    
    elif  i%5 == 0:
        five_list.append(i)
        
    elif  i%7 == 0:
        seven_list.append(i)
        
    elif  i%9 == 0:
        nine_list.append(i)
        
for i in list2:
    if i%4 == 0:
        four_list.append(i)
    
    elif  i%6 == 0:
        six_list.append(i)
        
    elif  i%8 == 0:
        eight_list.append(i)
        
    elif  i%10 == 0:
        ten_list.append(i)
        
    elif  i%3 == 0:
        three_list.append(i)
    
    elif  i%5 == 0:
        five_list.append(i)
        
    elif  i%7 == 0:
        seven_list.append(i)
        
    elif  i%9 == 0:
        nine_list.append(i)

#printing each list  
print("\nList Containing Numbers from the list 1 & List 2 which are Divisible by 4 is:")
print(four_list)
    
print("\nList Containing Numbers from the list 1 & List 2 which are Divisible by 4 is:")
print(six_list)
    
print("\nList Containing Numbers from the list 1 & List 2 which are Divisible by 4 is:")
print(eight_list)
    
print("\nList Containing Numbers from the list 1 & List 2 which are Divisible by 4 is:")
print(ten_list)
    
print("\nList Containing Numbers from the list 1 & List 2 which are Divisible by 4 is:")
print(three_list)
    
print("\nList Containing Numbers from the list 1 & List 2 which are Divisible by 4 is:")
print(five_list)
    
print("\nList Containing Numbers from the list 1 & List 2 which are Divisible by 4 is:")
print(seven_list)
    
print("\nList Containing Numbers from the list 1 & List 2 which are Divisible by 4 is:")
print(nine_list)


        

        