class employee:
    # lan="Python",
    # salary=45438

    def __init__(self,name, salary, lan):  # this is known as constructor it call automatically when ever an object created
        self.name=name,
        self.salary=salary,
        self.lan=lan
        print("I am creating an object")

    @staticmethod
    def greet():
        print("Glooo")
        
yash=employee("Yash is good",233434,"C++")

print(yash.name,yash.lan, yash.salary)