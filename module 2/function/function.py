
MARKS = []


def get_marks():
    no_of_subjects = int(input("Enter the number of subjects that you want:"))

    for i in range (0,no_of_subjects,1):
        value = int(input(f"Enter the mark obtained in {i+1} subject:"))
        MARKS.append(value)



def get_info():
    name = input("Enter the NAME of student")
    Class = input("Enter the CLASS of student")
    roll = int(input("Enter the Roll number of student"))
    global NAME
    global CLASS
    global ROLL
    NAME = name
    CLASS = Class
    ROLL = roll


def get_result():
    obtained_mark = 0
    for i in range (len(MARKS)):
        obtained_mark = obtained_mark + MARKS[i]
    print(f"student name {NAME} of class {CLASS} with roll no {ROLL} have obtained {obtained_mark}")


get_info()
get_marks()
get_result()



