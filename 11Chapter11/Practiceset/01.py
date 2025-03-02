class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The vecor is {self.i}i + {self.j}j")


class ThreeDVector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"The vecor is {self.i}i + {self.j}j+ {self.k}k ")

a=twoDvector(1,2)
b=ThreeDVector(1,2,3)

a.show()
b.show()


