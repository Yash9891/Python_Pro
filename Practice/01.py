# a=34.5
# name='Popo iosm'
# print(type(a))
# print(type(name))

# a='56'
# num=int(a)
# print(num+10)

# numi=90
# stri=str(numi)
# print(stri+'900 is ')

# nu=90
# fl=float(nu)
# print(nu+24.5)

#String------------------------------
# name="yash is a good boy"
# print(name[1:6])
# print(name[-3:])
# print(name[0:10:2])
# print(len(name))
# print(name.endswith('boy'))
# print(name.count("b"))
# print(name.capitalize())
# print(name.find("is"))
# print(name.replace("yash","New yash boy"))
# print(name.isalpha())
# print(name.lower())
# print(name.upper())


#List------------------------------------

# list =[45,67,23,"Yash",'Atharv']

# print(list[3])
# print(list[3:5])
# print(list[-4:])

# l1 = [1,8,7,2,21,15]
# l1.sort()
# l1.reverse()
# l1.append(340)
# l1.insert(2,4000)
# l1.remove(8)
# l1.pop()
# print(l1)


#Tuple----------------------------------------
# a=()#empty tuple

# a=(1,7,2,2,1,3,1)
# print(a.count(1))
# print(a[1])
# print(a[1:])
# print(len(a))
# print(a.index(3))
# print(a)

#Dictionary-----------------------------------

# dic={
# "name":"harry",
# "from":"india",
# "marks":[92,98,96]    
# }
# print(dic.items())
# print(dic.keys()) 
# print(dic.values()) 
# dic.update({"friends":"Atharv"})
# print(dic.get("name"))
# dic.pop("name")
# # dic.clear()
# print(dic) 

# print(dic["friends"])
# print(dic["marks"])
# print(dic["marks"][0:2])
# for item in dic["marks"]:
#     print(item)


#set------------------------------------------
# s=set()
# s.add(34)
# s.add(4)
# print(s)


# s={1,4,6,72,1}
# # s.pop()
# # s.remove(4)
# # s.clear()
# s.add(45)
# newset=s.union({43,67,342,23,45})
# print(len(s))
# print(s)
# print(newset)
# print(s.intersection({45,2,1,3,43}))


#if else-------------------------------------

# post="yash is going to visit his friend and Atharv will come to meet him"
# if("Yash".lower() in post.lower()):
#     print("Yash is present")
# else:
#     print("yash is not present")

#loops---------------------------------------
# i =1
# while(i<5):
#     print(f"Heloo yash ${i}")
#     i+=1

# for i in range(2,11,2):
   
#     if(i==8):
#         break
#     print(i,end=' ')

# else:
#     print("Done")


# l=[45,24,23,4]
# for i in l:
#     pass


# row=3

# for i in range(1,row+1):
#     for j in range(row-i):
#      print(" ", end="")
#     for k in range(1,2*i):
#      print("*", end="")
#     print()


# row=6
# col=5
# for i in range(1,row+1):
#     for j in range(1, col+1):
#         if(i==1 or i==row or j==1 or j==col):
#             print("*",end=" ")
#         else:
#             print(" ", end=' ')
#     print()
 

# def greet(name):
#     print(f"{name}, You are intelegent")
    
# list=["Yash Kumar","Atharv Grover","Arayan Saini","Akshay Saini"]
# for nam in list:
#     first=nam.split()[0]
#     greet(first.upper())


# def fact(num):
#     if(num==0 or num==1):
#         return 1
#     return num*fact(num-1)
# print(fact(3))

# def sumi(num):
#     if(num==1):
#         return 1
#     return num+sumi(num-1)
# print(sumi(5))

# def pat(row):
#     if(row==0):
#         return
#     print("*"*row)
#     pat(row-1)

# pat(3)

# f=open("Write.txt","w")
# f.write("Yash is a good\n boy i have ever seen\n but Atharv is not")
# f.close()

# with open("write.txt") as file:
#     data=file.read()
#     print(data)
# if("Yash" in data):
#     print("Yash is present")

with open("Write.txt","a") as file:
    file.write("\nYo ho how are you")

