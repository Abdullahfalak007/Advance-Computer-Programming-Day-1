# =============================================================================
# Write a program which asks the user to enter time of the day from the user in 
# hours. Then greets the user according to the time he/she enters. If the time 
# is less than 10, create a “Good morning” greeting. If not, but time is less 
# than 20, create a “Good day” greeting, otherwise a “Good Night”.
# =============================================================================

#taking interger input in variable time
time = int(input("\nEnter the time of the day in hours: "))

#using conditionals to print the respective string
if time<10:
    print("\n GOOD MORNING")

elif time<20:
    print("\n GOOD DAY")
    
else:
    print("\n GOOD NIGHT")