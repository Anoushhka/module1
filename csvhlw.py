
import csv

# function to get student information

def get_student_info():
    name = input("Enter student's name:")
    age = int(input("Enter student's age:"))
    job = input("Enter student's job:")
    return {"name":name, "age":age, "job":job}

# function to save student information to a csv file

def save_student_info(student, filename="students.csv"):
    with open(filename, mode='a',newline='')as file:
        writer= csv.DictWriter(file,fieldnames=["name","age","job"])
        writer.writerow(student)


# function to list students with age greater than 15
def list_students_age_greater_than_15(filename="students.csv"):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        print("\nStudents whose age is greater than 15:")
        for row in reader:
            if int(row["age"]) > 15:
                print(f"Name: {row['name']}, Age: {row['age']}, Job: {row['job']}")

def main():
    while True:
        choice = input("\nChoose an option:\n1. Add a new student\n2. List students whose age is greater than 15\n3. Quit\nEnter your choice: ")
        if choice == '1':
            student = get_student_info()
            save_student_info(student)
        elif choice == '2':
            list_students_age_greater_than_15()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    # Create the CSV file with headers if it doesn't exist
    with open("students.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "job"])
        writer.writeheader()
    
    main()
