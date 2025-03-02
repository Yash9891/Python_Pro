class programmers:
    company="Micorsoft"
    def __init__(self, name, salary, department):
        self.name=name,
        self.salary=salary,
        self.department=department

    @staticmethod 
    def work():
            print("Programmers always do work ")

yash=programmers("Yash",45089,"delhi")
piyush=programmers("Piyush",45089,"noida")
aman=programmers("Aman",45089,"gurugram")

aman.work()
print(yash.name,aman.name,piyush.department,yash.company,aman.company)