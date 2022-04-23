student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

#sum(student_heights)//different way to perform
total_height = 0
for height in student_heights:
    total_height = total_height + height
print(total_height)

    # len(student_heights)// other way to perform
number_student = 0
for student in student_heights:
    number_student += 1
print(number_student)

average_height = round(total_height / number_student)
print(average_height)

# max function
highest_height = 0
for height in student_heights:
    if height > highest_height:
        highest_height = height
print(f"The highest height in the class is:{highest_height}")





