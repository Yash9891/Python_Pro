#Find the gratest-------------------------------

# def gre(a,b,c):
#     if(a>b):
#         if(b>c):
#             print(f"{a} is greater")
#         else:
#             print(f" {c} is greater")
#     else:
#         if(b>c):
#             print(f"{b} is greater")
#         else:
#             print(f" {c} is greater")

# gre(34,65,21)
# gre(34,65,241)
# gre(343,65,21)

#----Convert f to celcius----------------------
# def ftoc(fer):
#     c=5*(fer-32)/9
#     return c
# num=int(input("Enter the tem in Fernhite"))
# print("IN celcius",round(ftoc(num),2))


# calculate sum of 1st natural num using recursion----------


# def rec(num):
#     if(num==0):
#         return 0
#     return num + rec(num-1)
# print(rec(5))


#--------------remove a word and strip it in list


def rm(list, word):
    n=[]
    for item in list:
        if not(item==word):
            n.append(item.strip(word))
    return n
        
list=["Yash","HarryDog","Batman","Dog"]
print(rm(list,"Dog"))