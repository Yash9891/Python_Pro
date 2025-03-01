# num= int(input("ENter a number "))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i} ")


# names=["Harry","Sapna","Suman","Yash","Shivam","Kumpot"]

# for name in names:
#     if(name[0].lower()=="s"):
#         print(f"Good morning, {name}")
 


#--------------Prime or not---------------

# num= int(input("Enter a number "))

# for i in range(2,num):

#         if(num%i==0 ):
#             print("This is not prime")
#             break
# else:
#     print("This is prime")



#--------------sum of first natural num--------------------
# num =int(input("ENtyer a number"))
# sum=0
# for i in range(1,num+1):
#     sum=sum+i
# print(sum)


#--------------factorial-----------------------
# num= int(input("Enter a number "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i

# print(fact)

#---------------Star pattern-------------------

# *
# **
# ***

# for i in range(1,4):
#     for j in range(i):
#         print(" ",end="")
#         print()


#-----------------------------------------------------
#    *
#   ***
#  *****

# row=3
# for i in range(1,row+1): # rows =3
#     for j in range(row-i): 
#         print(" ",end="")
#     for k in range(1,2*i): # columns=5
#         print("*", end="")
#     print()

row=5
col=5
for i in range(1,row+1):
    for j in range(1,col+1):
        if(i==1 or i== row or j==1 or j==col):
            print("*",end="")
        else:
            print(" ", end="")
    print()

        
