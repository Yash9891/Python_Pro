words=["donkey","fool","fraud"]


with open("./09Chapter9/Practiceset/sensor.txt", "r") as file:
    data=file.read()
for word in words:
    data=data.replace(word,"######")
with open("./09Chapter9/Practiceset/sensor.txt", "w") as file:
    file.write(data)