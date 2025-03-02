class demo:
    a=4

    @staticmethod
    def greet():
        print("Kloo bha")

o=demo()
print(o.a)
o.a=0   # it does not change class attribute
print(o.a)
print(demo.a)
print(o.greet())

