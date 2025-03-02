from random import randint
class trains:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in train no :{self.trainNo} from {fro} to {to}")
    def getstatus(self):
        print(f"Train no {self.trainNo} is running")
    def getfair(self,fro,to):
         print(f"Thicked is booked in train no :{self.trainNo} from {fro} to {to} is {randint(222,555)}")
 
t=trains(12399)
t.book("Rampur","delhi")
t.getstatus()
t.getfair("Delhi","Ghaziabad")