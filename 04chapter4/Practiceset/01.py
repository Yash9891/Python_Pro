list=[]
for i in range(7):
    fruits=input(f"ENter the fruit name {i} ")
    list.append(fruits)
print(list)

marks=[]
for i in range(4):
    mark=int(input(f"ENter the mark of student {i}"))
    marks.append(mark)
marks.sort()
print(marks)

sum=0
for i in range(4):
    num=int(input("Enter the number "))
    sum=sum+num
print(sum)

l=[34,23,3,2,4,2]
print(sum(l))


tup=(3,4,5,2,0,5,0,3,0,0,0,45)
print(tup.count(0))