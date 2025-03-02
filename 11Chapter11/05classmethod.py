# you can access class directly inside a method

class Employee:
    a=1
    
    def show(self):
        print(f" the value of a is {self.a}")  #It shows instance attribute
    
    @classmethod
    def show2(cls):
        print(f" the value of a is {cls.a}")  #It shows class attribute


e=Employee()
e.a=45

e.show()  # show the object attribute
e.show2() # show the class attribute