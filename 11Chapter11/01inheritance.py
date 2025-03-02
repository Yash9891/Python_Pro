class employee:
    company ="ITC",
    name="Yash",
    salary=9000000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")



#If you use this method if you chnage some method in employee clas then you claspo need to chnag ein eprogrmammer also
# class Programmer:
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def lan(self):
#         print(f"The name is {self.name} and the language is {self.language}")



#Inheritance--------------------------------
class Programmer(employee):
    company="Iti infotech"
    def lan(self):
        print(f"The name is {self.name} and the language is {self.language}")

a=employee()
b=Programmer()

print(a.company,b.company)
b.show()