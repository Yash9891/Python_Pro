# text=input("Enter the text ")
# if("danger" in text or "hurry" in text or "money" in text):
#     print("Fraud")
# else:
#     print("Good text")

dangers=["danger","money","urgent","fast","give","outside"]
text=input('Enter you post ')
dan=False
for word in dangers:
    if(word in text.lower()):
        dan=True
        break

if(dan==True):
    print(" Fraud ")
else:
    print("SAfe")
