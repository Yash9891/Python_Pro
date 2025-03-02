# class is the blueprint to create object

class employee: 
    language="Hindi", # class attributes
    salary=900000

object1=employee()
object1.name="Yash is good" # this is object attribute (instance attribute)
print(object1.name,object1.language,object1.salary)

rohan=employee()
rohan.name="Rohan is not good"  # this is object attribute (instance attribute)
print(rohan.name,rohan.salary,rohan.language)
