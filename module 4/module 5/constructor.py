class Human:
    
  def __init__ (self,name,gender,age): #constructor function
    self.name = name
    self.gender = gender
    self.age = age

h1 = Human("kushal","male","24")
h2 = Human("Tanisha","female","19")

print(h1.name,h1.gender,h1.age)
print(h2.name,h2.gender,h2.age)

