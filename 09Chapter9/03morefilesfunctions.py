f=open("file.txt","r")

# content=f.readlines()

# print(content,type(content))

line1=f.readline()
line2=f.readline()
line3=f.readline()

print(line1)
print(line2)
print(line3)

f.close()