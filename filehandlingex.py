# student ko info file ma gayera store hunaparyo

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
    print(f"The name of the student is {name} class of the student is{Class} and roll no is {roll}")


 
get_info()

Text = ""

with open ("student.txt","w") as file:
    file.write(NAME)
    file.write(CLASS)
    file.write(str(ROLL))

print("Writing Sucess !! ")


with open("student.txt","r") as file:
       text = file.read()

print(text)


new_message = " hi "

with open("student.txt",'a') as file:
    file.write(new_message)  