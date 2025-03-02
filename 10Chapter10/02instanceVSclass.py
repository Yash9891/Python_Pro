
#INstance attributes take over class attributes 
class employee: 
    language="Hindi", # class attributes
    salary=900000


rohan=employee()
rohan.language="Java script"  # this is object attribute (instance attribute)
print(rohan.salary,rohan.language)
