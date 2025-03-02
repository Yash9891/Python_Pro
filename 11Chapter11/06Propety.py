# property decorator

class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=Employee()
e.name='Yash saini'
print(e.lname)  
e.show()