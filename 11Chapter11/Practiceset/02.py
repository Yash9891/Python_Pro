class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def walk(self):
        print('I am waliking')


class pets(animal):
    def __init__(self,name,age,food):
        super().__init__(name,age)
        self.food=food
    def eat(self):
        print("I am eating")

class dog(pets):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)  # Call Pets constructor
    def bark(self):
        print("I am barking")
  
a=animal("Yash",45)
p=pets("Biskut",67,"Lol")

p.eat()

ob1=dog("Yhu",67,"pop")
ob1.bark()
ob1.eat()
ob1.walk()