#MAX number-------------------------------

# arr=[45,65,23,90,11,23,12]
# max=0
# for i in range(0, len(arr)):
#     if(arr[i]>max):
#         max=arr[i]
# print(max)


#MIN NUMBER-------------------------------

# arr=[45,65,23,90,11,3,23,12]
# def minnum(arr):
#     min=arr[0]
#     for i in range(0, len(arr)):
#         if(arr[i]<min):
#             min=arr[i]
#     return min

# 2nd minimum---------------------------
# def seconmin(arr):
#     min1=minnum(arr)
#     min2 = float('inf')  # Set second min to a large value initially

#     for i in range(0, len(arr)):
#         if(min2>arr[i] and arr[i]>min1):
#             min2=arr[i]
#     return min2 

# print(minnum(arr))
# print(seconmin(arr))



#2nd MAX number-------------------------------

# arr=[45,65,56,92,23,90,11,23,12]
# arr.sort()
# print(arr[-2])

#Reverse an array-----------------------------------------
# arr=[1,2,3,4,5,6,7,8,9,10]

 # 1st method
# print(arr[::-1])

#2nd method


# def reverseArr(arr):
#     arr2=[]
#     for i in range(len(arr)):
#         arr2.append(arr[len(arr)-i-1])
#     return arr2
# arr=reverseArr(arr)
# print(arr)


#Count frequencry of each element in an array------------------------
arr = [10, 5, 10, 15, 10, 5]

# Dictionary to store frequency counts
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Printing frequencies
for key, value in freq.items():
    print(f"{key} count = {value}")



