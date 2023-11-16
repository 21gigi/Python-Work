name = input("Name: ")
math = float(input("Math: "))
science = float(input("Science: "))
english = float(input("English: "))

average = (math + science + english) / 3
print("Average: {:,.1f}".format(average))

if average >= 75:
    if math < 75:
        print("Congratulations! You passed the semester. But you have to re-enroll Math subject")
    elif science < 75:
        print("Congratulations! You passed the semester. But you have to re-enroll Science subject")
    elif english < 75:
        print("Congratulations! You passed the semester. But you have to re-enroll English subject")
    else:
        print("Congratulations! You passed the semester without any failed subject.")
else:
    print("Sorry. You failed the semester.")
