#Question 1: Write a Python program to Reverse a String.--------------

# s="Heloo kese ho yash"
# # print(s[::-1])

# rev=""
# for i in range(len(s)): 
#     rev=s[i]+rev
# print(rev)
 
# Question 2: Write a Python program to Check Palindrome.-------------------

# def palindrome(strin):
#     s=strin.replace(" ","")
#     if(s[::-1].lower()==s.lower()):
#         return True
#     else: 
#         return False

# a="Mom mom"
# if(palindrome(a)):
#     print("String is palindrome")
# else:
#     print("String is not palindrome")


#for number palindrome---------------------------
# def palindrome(num):
#     str_num=str(num)
#     if(str_num[::-1]==str_num):
#         return True
#     else:
#         return False
# num=1218
# if(palindrome(num)):
#     print("This is palindrome")
# else:
#     print("This is not palindrome")


# Question 3: Write a Python program to Count Vowels in a String.--------------------


# def count_vowels(title):
#     count=0
#     vowels=["a","e","i","o","u"]
#     for char in title:
#         if char in vowels:
#             count+=1
#     return count

# title="The Godzilla minus one"
# print(f"The num of vowels is {count_vowels(title)}")


# Question 4: Write a Python program to find Factorial with Recursion.------------

# def fact(num):
#     if( num==0 or num==1):
#         return 1
#     return num*fact(num-1)

# num=6
# print(f"The factorial of {num} is {fact(num)}")


# without recursion

# num=1
# fact=1
# if(num<0):
#     print("Fact is not defined for negative numbers")
# else:
#     for i in range(1,num+1):
#         fact=fact*i
#     print(fact)


# Question 5: Write a Python program to find Fibonacci Sequence.--------------
# def fibo(n):
#     lst=[0,1]
#     for i in range(2,n):
#         new_num=lst[-1]+lst[-2]
#         lst.append(new_num)
#     return lst

# num_terms=10
# print(fibo(num_terms))

#Question 6: Write a Python program to find the Maximum Element in a List.-----------------------

# def max_num(list):
#     maxi=list[0]
#     for item in list:
#         if(item>maxi):
#             maxi=item
#     return maxi
# list=[452,53,23,254,1423,5600]

# print(f"The max element is {max_num(list)}")


#Question 7: Write a Python program to find Anagram Check.-------------------

# def anagram(a,b):
#     new_a=a.replace(',','').lower()
#     new_b=b.replace(',','').lower()
#     if(sorted(new_a)==sorted(new_b)):
#         return True
    
#     else:
#         return False
# a="listen Is good, boy,"
# b="boy is, silent ,,good"
# if(anagram(a,b)):
#     print("This is anagram")
# else:
#     print("This is not anagram")


#Question 8: Write a Python program to find Prime Numbers.-----------------

# def prime(num):
#     if(num<=1):
#         return False
#     for i in range(2, num):
#         if(num%i==0):
#             return False
#     return True

# if(prime(66)):
#     print("This is prime")
# else:
#     print("Not prime")


#Question 9: Write a Python program to find the Minimum Element in a List.-----------------

# def min_num(lst):
#     mini=lst[0]
#     for el in lst:
#         if(mini>el):
#             mini=el
#     return mini
# lst=[-4,1,23,65,2,4]
# print(f"The min num is {min_num(lst)}")

#Question 10: Write a Python program to calculate the Sum of Digits in a Number.-------------------

# def digit_sum(num):
#     new_num=str(num)
#     sum=0
#     for digit in new_num:
#         sum=sum+int(digit)
#     return sum

# num=123459
# print(f"Sum of digits is {digit_sum(num)}")


#Question 11: Write a Python program to check for Armstrong Number.
#A number that is equal to the sum of its own digits each raised to the power of the number of digits. 

# def armstrong(num):
#     new_num=str(num)
#     power=len(new_num)
#     sum=0
#     for digit in new_num:
#         sum=sum+int(digit)**power
#     if(sum==num):
#         return True
#     else:
#         return False 

# num=3709
# if(armstrong(num)):
#     print("This is an armstrong num")
# else:
#     print("This is not armstrong num")

#Question 12: Write a Python program to check for Leap Year.------------

# def leap_year(year):
#     if((year%4==0 and year%100!=0) or year %400==0):
#         return True
#     else:
#         return False

# year=2032
# if(leap_year(year)):
#     print("This is a leap year")
# else:
#     print("This is not a leap year")

#Question 13: Write a Python program to find the Average Numbers in a List.-----------
# lst=[10, 20, 30, 40, 50]
# length=len(lst)
# sum=0
# for i in range(0,length): 
#     sum=sum+lst[i]
# average=sum/length
# print(f"The avg is {round(average,2)}")

#Question 14: Write a Python program to Merge Two Sorted Lists.------------------
# def mergelists(list1,list2):
#     newlist=[]
#     i=0
#     j=0

#     while(i<len(list1) and j<len(list2)):
#         if(list1[i]<list2[j]):
#             newlist.append(list1[i])
#             i+=1
#         else:
#             newlist.append(list2[j])
#             j+=1
#     while(i<len(list1)):
#         newlist.append(list1[i])
#         i+=1      
#     while(j<len(list2)):
#         newlist.append(list2[j])
#         j+=1
#     return newlist

# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 6, 8, 10,11,16]
# print(mergelists(list1,list2))

#Question 15: Write a Python program to Remove Duplicates from a String..................

# def remove_duplicates(string):
#     unique_chars=set()
#     result=""
#     for char in string:
#         if char not in unique_chars:
#             unique_chars.add(char)
#             result+=char
#     return result
   
# string="hello world yash"
# print(remove_duplicates(string))

#Question 16: Write a Python program to Check for Perfect Numbers.--------------
#A positive integer that is equal to the sum of all its positive divisors, except for the number itself. For example, 6 is a perfect number because 1 + 2 + 3 = 6. 

# def perfect_num(num):
#     if(num<=0):
#         return False
#     diviosor_sum=0
#     for i in range(1,num):
#         if( num%i==0):
#             diviosor_sum+=i
#     return diviosor_sum==num
   
# num=28
# if(perfect_num(num)):
#     print("This is a perfect num")
# else:
#     print("This is not a perfect num")

#Question 17: Write a Python program to check if a Number is Even or Odd------
# def even_odd(num):
#     if(num%2==0):
#         print("Even")
#     else:
#         print("Odd")
# even_odd(35)

#Question 18: Write a Python program to Count Words in a Sentence.
def count_words(sentence):
    words=sentence.split()
    return len(words)
sentence = "This is a sample sentence."

print("The number of words is", count_words(sentence))