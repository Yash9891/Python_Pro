#Multiple inheritance------------------------

class employee:
    company ="ITC",
    name="Yash",
    salary=9000000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class coder:
    language="Python"
    def lani(self):
        print(f"Language is {self.language}")

class Programmer(employee,coder):
    company="Iti infotech"
    def lan(self):
        print(f"The name is {self.name} and the language is {self.language}")

a=employee()
b=Programmer()

print(a.company,b.company)
b.show()
b.lani()