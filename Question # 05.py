# =============================================================================
# Write a program that takes 10 student marks from the user in the LIST using 
# loop, calculate the average and shows the highest and lowest marks, assign 
# grade to each student. (Grade: A+>90, A>80, B+>70, B>60, C>50, D>40, F<40)
# =============================================================================

#taking input of ten students
print("Enter Marks Obtained by 10 Students: ")
Student1 = int(input("Marks of First Student:"))
Student2 = int(input("Marks of Second Student:"))
Student3 = int(input("Marks of Third Student:"))
Student4 = int(input("Marks of Fourth Student:"))
Student5 = int(input("Marks of Fifth Student:"))
Student6 = int(input("Marks of Sixth Student:"))
Student7 = int(input("Marks of Seventh Student:"))
Student8 = int(input("Marks of Eighth Student:"))
Student9 = int(input("Marks of Nineth Student:"))
Student10 = int(input("Marks of Tenth Student:"))

#Adding the number of all students
sum_of_marks = Student1 + Student2 + Student3 + Student4 + Student5 + Student6 + Student7 + Student8 + Student9 + Student10

#calculatin the average
avg_of_marks = sum_of_marks / 10

mylist = [Student1, Student2, Student3, Student4, Student5, Student6, Student7, Student8, Student9, Student10 ]

#to calculate the minimum marks
min_marks = mylist[0]

for i in range(0,len(mylist)):
    if(mylist[i] < min_marks):
        min_marks = mylist[i]

print("\n{}{}".format("Minimum marks Obtained are :", min_marks))

#to calculate the maximum marks
max_marks = mylist[0]

for i in range(0,len(mylist)):
    if(mylist[i] > max_marks):
        max_marks = mylist[i]

print("{}{}".format("Minimum marks Obtained are :", max_marks))

#fucntion def to calculate the grades
def cal_grades(marks):
    if marks>=91 and marks<=100:
        print("Your Grade is A+")
    elif marks>=81 and marks<91:
        print("Your Grade is A")
    elif marks>=71 and marks<81:
        print("Your Grade is B+")
    elif marks>=61 and marks<71:
        print("Your Grade is B")
    elif marks>=51 and marks<61:
        print("Your Grade is C")
    elif marks>=41 and marks<51:
        print("Your Grade is D")
    elif marks<41:
        print("Your Grade is F")
    else:
        print("Invalid Input!")
        
#caliing the above function for each student
print("Grade of First Student:")
cal_grades(Student1)
print("Grade of Second Student:")
cal_grades(Student2)
print("Grade of Third Student:")
cal_grades(Student3)
print("Grade of Fourth Student:")
cal_grades(Student4)
print("Grade of Fifth Student:")
cal_grades(Student5)
print("Grade of Sixth Student:")
cal_grades(Student6)
print("Grade of Seventh Student:")
cal_grades(Student7)
print("Grade of Eighth Student:")
cal_grades(Student8)
print("Grade of Nineth Student:")
cal_grades(Student9)
print("Grade of Tenth Student:")
cal_grades(Student10)
