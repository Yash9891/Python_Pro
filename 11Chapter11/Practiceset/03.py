class employee:
    salary=80
    increment=20

    @property
    def afterincre(self):
        return self.salary+self.salary*(self.increment/100)
    @afterincre.setter
    def afterincre(self,salary):
        self.increment=((salary/self.salary)-1)*100

e=employee()
# print(e.afterincre)

e.afterincre=280  #it change the increment property
print(e.increment)