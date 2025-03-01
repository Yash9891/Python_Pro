def fact(num):
    if(num==1 or num==0):
        return 1
    return num*fact(num-1)
n=int(input("ENter a num "))
print(f"Fact of {n} is ",fact(n))