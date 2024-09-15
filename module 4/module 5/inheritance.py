class Parent:
    def __init__(self):
        pass

    def are_tall(self):
        return True


class Child(Parent): #inherit garney kura
    def __init__(self):
        pass


c1 = Child()
x = c1.are_tall()
if x :
    print ("child are tall")