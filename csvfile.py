
import csv

# with open ("data.csv","w") as file:
#     file.write("ram,10,24")

# print("Writing done!!")

#list of dictionaries
student = [{"name":"Tanisha","class":12,"roll":17} ,{"roll":20,"name":"shyam","class":9}]

with open ('data.csv','w') as file:
   fieldname = ['name','class','roll']
   writer = csv.DictWriter(file,fieldnames=fieldname)
   writer.writeheader()
   writer.writerows(student)


with open('data.csv','r') as file:
    reader = csv.DictReader(file,delimiter=',')
    for row in reader:
         print(row.get('name'))
         print(row)
        
# info chai input ma
# # ask student information as input and store them in csv file
# #add age to a student
# make sure the student information input consist a function to handle job
# list all the students whose age is greater than 15