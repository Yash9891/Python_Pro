
with open("./09Chapter9/Practiceset/donkey.txt", "r") as file:
    data=file.read()
data=data.replace("donkey","######")
with open("./09Chapter9/Practiceset/donkey.txt", "w") as file:
    file.write(data)