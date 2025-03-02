
#INstance attributes take over class attributes 
class employee: 
    language="Hindi", # class attributes
    salary=900000

    def getInfo(self): # self is use to accept the object in class
        print(f"The language is {self.language}, The salary is {self.salary}")
    
    def greet(self):
        print("Good morning")

    @staticmethod  # static method is decoractor where we mark it as is does not need object
    def noobject():
        print("For static method no need for object")


rohan=employee()
rohan.language="Java script"  # this is object attribute (instance attribute)
print(rohan.salary,rohan.language)

rohan.getInfo() # => it get convert into this -> employee.getInfo(rohan)
rohan.greet()
rohan.noobject()
