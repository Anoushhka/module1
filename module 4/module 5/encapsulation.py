class MyClass:
    def __init__(self):
        self._x = None
    
    def show(self):
        print(self._x)

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x (self,value):
        self._x = value
    
m = MyClass()
m._x = 10
m.show()