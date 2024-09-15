class Human:
    
    def __init__ (self,name,gender,age): #constructor function
        self.name = name
        self.gender = gender
        self.age = age

    def check_vote(self):
        if self.age>18:
            print(f"(self.name)can vote")
        else:
            print(f"{self.name})can't vote")

    def __str__(self):
        return f"{self.name},{self.gender},{self.age}"
   



h1 = Human("kushal","male",24)
h2 = Human("Tanisha","female",19)
h3 = Human("geeta","female",8)
print(h1)
print(h2)
print(h3)

# h1.check_vote()
# h2.check_vote()
# h3.check_vote()

# indentation ma dhyan