with open("twinkel.txt","r") as f:
    content=f.read()
with open("Renamed.txt","w") as f:
    f.write(content)