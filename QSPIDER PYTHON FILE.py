# 1. add two numbers
# a=int(input("enter the number :"))
# b=int(input("enter the number :"))
# print(a+b)
# print(f"the total value is {a+b}")

# 2. WAPTF the square of the number:
# c=int(input("enter the number :"))
# print(f"the square of the {c} is: {c**2}")

# 3. WAPT change float to integer number:
# d=float(input("enter a number:"))
# e=int(d)
# print(e,type(e))

# 4. WAPT print the last char form string:
# f=input(" enter a name:")
# print(f" the last char of {f} is : {f[-1]}")

# 5. WAPT reverse the string:
# g=input("enter name:")
# print(f"the reverse of '{g}' is : {g[::-1]}")


# 6. WAPT fetch middle value from list:
# h=eval(input("enter value:"))
# print([len(h)//2])

# 7. WAPT  extarct last number from value:
# i=(input("enter number:"))
# print(f"the last value of {i} is  : {i[-1]}")
# **************************************[IF]********************************************************
# 8. WAPT simple if program
# j=int(input("enter a number:"))
# if j%2==0:
#     print(f"{j} is even number ")

# 9.WAPT CHECK THE given string is exactly 5 char or not?:
# k=input("enter the  string:")
# if len(k)==5:
#     print(f"'{k}' is a five char")

# 10. WAP to check the given number is greater than 200 or not?
# m=int(input("enter the number:"))
# if m>200:
#     print(f"'{m}' is greater then 200.")

# 11. WAP to print the square of the number , if it's the multiple of 3 only:
# n=int(input("enter the  number:"))
# if n%3==0:
#     print(f" the square of '{n}' is  {n**2}")

#12. check the entered char is lower case or not?
# o = input("enter a char: ")
#
# if 'a' <= o <= 'z':
#     print(f"{o} is lower case")
# else:
#     print(f"{o} is not lower case")

#13. check the entered char is upper case or not?
# o = input("enter a char:")
#
# if 'A' <= o <= 'Z':
#     print(f"{o} is lower case")
# else:
#     print(f"{o} is not lower case")

# 14. WAP to find enter number is 3-digit number or not

# z=int(input("enter a number: "))
# if 99<=z<=999:
#      print(f"the enter  number is '{z}' is 3 digit")

# *********************************[IF-ELSE]****************************************

# 15.WAPT find enter number float number or not: note , if want check the type of data means,use TYPE()
# x=eval(input("enter a value:"))
# if type(x)==float:
#     print(f"the enter value'{x}' is float value")
# else:
#     print(f" '{x}' not a float value ")
#
# 16. WAPT find enter number is even number or  odd
# y=int(input("enter a number: "))
# if y%2==0:
#     print(f"the entered number '{y}' is even number")
# else:
#     print(f"the enter number '{y}' is odd number")

#17. WAP to check entered number is palaindrome or not:
# r=input("enter a values:")
# if r[::]==r[::-1]:
#     print(f"enter name '{r}' is palaindrome")
# else:
#     print(f"'{r}'not a palaindrome ")

#18. WAPT check thee given char is vowel or not:
# s=input("enter a char:")
# if s in ['a','e','i','o','u','A','E','I','O','U']:
#     print(f" the enter char '{s}' is vowel")
# else:
#     print(f" the enter char '{s}' not vowel")

#19. WAPT the enter value is single value datatype or multi value data type
#
# i=eval(input("enter a values:"))
# if type(i) in [int,float,complex]:
#     print(f"enter the values is '{i}' SVD")
# else:
#     print(f"enter the values is '{i}' MVD")

#20. WAP to check the given int is positive number or negative number
# a=int(input("enter a number: "))
# if 0<=a:
#     print(f"the given '{a}' is positive ")
# else:
#     print(f"the given '{a}' is negative ")

#21. WAP to check the given list has middle value or not? : use len() by even or odd
# b=eval(input("enter a value: "))
# if len(b)%2==1:
#     print(f"the given value has '{b}' middle value ")j
# else:
#     print(f"the given value it's doesn't have '{b}' middle value ")

#22. consider a tuple consists of only two values and check the tuple is homogenius or hetrogeinus
# c=eval(input("enter a tuple of values: "))
# if type(c[0])==type(c[1]):
#     print(f"the tuple is '{c}' homogenius")
# else:
#     print(f"the '{c}' tuple is both homo and hetro genius")

# **********************************[ELIF-CONDITION]********************************************

#23. WAP to check the relationship between two numbers:
# n1=eval(input("enter value for n1: "))
# n2=eval(input("enter value for n2: "))
# if n1==n2:
#     print(f"the relation between {n1} and {n2} are equal")
# elif n1>n2:
#     print(f"the relation between {n1} and {n2} are n1 is greater  than n2")
# elif n1<n2:
#     print(f"the relation between {n1} and {n2} are n1 is less than n2 ")

#24.  two corodinate thats x and y and check which coorander the data point are present
# x=eval(input("enter a value for x: "))
# y=eval(input("enter a value for y: "))
# if x>=0  and y>=0:
#     print(f"the {x} and {y} are present in first ")
# elif x>=0 and y<0:
#     print(f"the {x} and {y} are present in second ")
# elif x<0 and y<0:
#     print(f"the {x} and {y} are present in third ")
# else:
#     print(f"the {x} and {y} are present in fourth ")

#25. WAPT check the enter number is single , double, triple, or more than three digit number:
# u=eval(input("enter a number: "))
# if 0<=u<=9:
#     print(f"{u} is single digit")
# elif 10<=u<=99:
#     print(f"{u} is double digit")
# elif 100<=u<=999:
#     print(f"{u} is three digit")
# else:
#     print(f"{u} is more than three digit")

#26. WAPT check the enter char is lower or upper, number ?
# n=input("enter a value: ")
# if 'A'<=n<='Z':
#     print(f"the enter value '{n}' is U.char")
# elif 'a'<=n<='z':
#     print(f"the enter value '{n}' is L.char")
# elif '0'<=n<='9':
#     print(f"{n} its a digit")
# else:
#     print(f"{n} it's special char")

#27. WAPT predict the students results , based otained %
#  if score above 60% first class,
# if score above 85% distinct ,
# if score less than 60% 2nd class,
# if score below 35% fail

# n=eval(input("enter the score :"))
# if n>=85:
#     print(f"your score is '{n}' , so your are distinct student!")
# elif 61<=n<=85:
#     print(f"your score is '{n}' , so your are first class student!")
# elif 35<=n<=60:
#     print(f"your score is '{n}' , so your are second class student!")
# elif n<35:
#     print(f"your score is '{n}' , so your are failed student!")
#
#
# n=eval(input("enter the score: "))
# if 85<=n<=100:
#     print(f"your score is '{n}' , so your are distinct student!")
# elif 60<=n<=84:
#     print(f"your score is '{n}' , so your are first class student!")
# elif 35<=n<=59:
#     print(f"your score is '{n}' , so your are second class student!")
# elif n<35:
#     print(f"your score is '{n}' , so your are failed student!")
# else:
#     print(f"your enter wrong values:{n}")

# 28 1st greater number amoung the four number
# a=int(input("enter a first value: "))
# b=int(input("enter a second  value: "))
# c=int(input("enter a third value: "))
# d=int(input("enter a fourth value: "))
# if a>b and a>c and a>d:
#     print(f"a is greatest number here {a}")
# elif b>c and b>d:
#     print(f"b is greatest number here {b}")
# elif c>d:
#     print(f"c is greatest number here {c}")
# else:
#     print(f"d is greatest number here {d}")

# ***********************************[NESTED IF]************************************************
#30. WAP to check the given char is vowel or consentet
# n=input("enter the value: ")
# if 'a'<=n<='z' or 'A'<=n<='Z':
#     if n in "aieouAIEOU":
#         print(f"'{n}' is vowels")
#     else:
#         print(f"'{n}' is not an vowels")
# else:
#     print(f"'{n}' is not an alpha")

# 31. WAP to login into twitter by entering proper user name and password:
# user=input("enter your  user name: ")
# password=input("enter your password:")
# if user=="balaji":
#     if password=="1234":
#         print("your entering successfully")
#     else:
#         print("enter password is wrong")
# else:
#     print("wrong user name")

#32. proper logic for login page
# user=input("enter your  user name: ")
# if user=="balaji":
#     password = input("enter your password:")
#     if password=="1234":
#         print("your entering successfully")
#     else:
#         print("enter password is wrong")
# else:
#     print("wrong user name")

# 33. WAP to print reverse of the string only if it's starting with U.alphabet adn ending digit:
# a=eval(input("enter the string: "))
# if "A"<=a[0]<="Z":
#     if "0"<=a[-1]<='9':
#         print(a[::-1])
#     else:
#         print(f"enter string '{a}' last value is not end with number")
# else:
#     print(f"the entered string '{a}' is not start with U.alphabet char")

# 34. WAP find the greater number amoung the three number:
# a=eval(input("enter a number n1: "))
# b=eval(input("enter b number n2: "))
# c=eval(input("enter c number n3: "))
# if a>b:
#     if a>c:
#         print("a is greater")
# else:
#     if b>c:
#         print("b is greater")
#     else:
#         print("c is greater ")
#35. WAP to find smaller number in 3 number
# a=eval(input("enter the a:"))
# b=eval(input("enter the b: "))
# c=eval(input("enter the c: "))
# if a<b and a<c:
#     print(f"a is smaller number '{a}'")
# else:
#     if b<c:
#         print(f" b is smaller here '{b}'")
#     else:
#         print(f"c is smaller '{c}'")
# #36. WAPT check 2nd large number amoung 4 number
# a=int(input("enter a number :"))
# b=int(input(" enter b number: "))
# c=int(input(" enter c number: "))
# d=int(input(" enter d number: "))
# if a>b and a>c and a>d:
#     if b>c and b>d:
#         print("b is greater")
#     if c>d:
#         print("c is greater")
#     else:
#         print(" d is greater")
# elif b>a and b>c and b>d:
#     if c>d:
#         print("c is greater ")
#     else:
#         print("d is greater")
# elif c>a and c>b and c>d:
#     if d>c:
#         print("c is greater ")
#     else:
#         print("d is greater ")

# 36. another example for that above sum:
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# d = int(input("Enter d: "))
#
# # find largest first
# if a>b and a>c and a>d:
#     # now find 2nd largest among b,c,d
#     if b>c and b>d:
#         print("Second largest is:", b)
#     else:
#         if c>d:
#             print("Second largest is:", c)
#         else:
#             print("Second largest is:", d)
#
# else:
#     if b>a and b>c and b>d:
#         # largest is b → check a,c,d
#         if a>c and a>d:
#             print("Second largest is:", a)
#         else:
#             if c>d:
#                 print("Second largest is:", c)
#             else:
#                 print("Second largest is:", d)
#
#     else:
#         if c>a and c>b and c>d:
#             # largest is c → check a,b,d
#             if a>b and a>d:
#                 print("Second largest is:", a)
#             else:
#                 if b>d:
#                     print("Second largest is:", b)
#                 else:
#                     print("Second largest is:", d)
#
#         else:
#             # largest is d → check a,b,c
#             if a>b and a>c:
#                 print("Second largest is:", a)
#             else:
#                 if b>c:
#                     print("Second largest is:", b)
#                 else:
#                     print("Second largest is:", c)
#
#
# JUST EXAMPLESs:{
# print([1,2,3]==[3,2,1])
# print({1,2,3}=={3,2,1})
# print((1,2,3)==(3,2,1))
# print({'a':12}=={12:'a'})
# }
# *************************************[LOOPING STATEMENT]************************************************
#  WHILE LOOP: CONTINUE GIVE PRINT OUTPUT AGAIN ND AGAIN UNTIL THE CONDITION GET FAILED:
# 37. WAPT
# i=1
# while i<=10:
#     print("i took the class",i)
#     i=i+1

# 38. WAPT PRINT N NATURAL NUMBERS:
# n=int(input("enter a number :"))
# i=1
# while i<=n:#the user input
#     print(f"the natural numbers'{i}'")# the statement print again and again untile the condition fails.
#     i=i+1# update

# 38. WAPT extract the number between 1 to 10:
# i=1
# while i<=10:
#     if i%2==0:
#         print(f"even number '{i}'")
#     i=i+1
# **************************************************************************************

# EXAMPLES SUMS FROM GPT:
# 1. REVERSE NUMBERS
# i=10
# while i>=1:
#     print(i)
#     i=i-1

# #2. ASK PASSWORD UNTIL IT'S CORRECT:
# pd='1234'
# u=input("enter the password")
# i=1
# while u!=pd:
#     print(input("password wrong , enter again"))
# # *************
# pd='1234'
# u=input("enter the password: ")
# i=1
# while u!=pd:
#     u=(input("password wrong , enter again"))
# print('password correct')
#**********************************************************************************
# # 39 WAPT print all the numbers which are multi of 5,between 1 to n:
# n=int(input("enter a number: "))
# i=1
# while i>=n:
#     if n%5==0:
#         print(n)
#     i=i+1


# 40. wap to fetch the number , divide by 2 and 5 between 100:
# i=1
# while i<=100:
#     if i%2==0 and i%5==0:
#         print(i)
#     i=i+1

# # 41. WAP a program to print 2 tables:
# i=1
# while i<=10:
#     print(i,'x = ',i*2)
#     i=i+1

# # 42. WAPT reverse the  order
# i=int(input("enter a number: "))
# while i>=1:
#     print(i)
#     i=i-1

# 42. WAPT reverse the integer number:
# n=int(input("enter a integer: "))
# i=n
# rev=0
# while i>0:
#     ld=i%10
#     rev=rev*10+ld
#     i=i//10
# print(rev)

# # 43. WAPT find the sum the individual digits
# n=int(input('enter a number: '))
# sum=0
# i=n
# while i>0:
#     ld=i%10
#     sum=sum+ld
#     i=i//10
# print(sum)
# # wap program, itration for sum and  reverse
# # 44. WAPT FIND THE PRODUCT OF EVEN INDIVIDUAL DIGITS:
# N=int(input("enter a number :"))
# even=0
# sum=0
# i=N
# while i>0:
#     ld=N%10
#     if i%2==0:
#         even=even*10+ld
#         sum=sum+even
#         i=i//10
#
# print(sum)
# #  44. WAPT FIND THE PRODUCT OF EVEN INDIVIDUAL DIGITS:
# n=int(input("enter a number: "))
# product=1
# i=n
# while i>0:
#     ld=i%10
#     if ld%2==0:
#        product=product*ld
#     i=i//10
# print(product)

# 45.  WAPT find sum of natural numbers:
# n=int(input("enter a number: "))
# i=1 ?????????????
# sum=0
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)
# 46.  wap find factorial number:


# 47. wapt print the every char in string:
# n=input("enter a string: ")
# i=0
# while i<len(n):
#     print(n[i])
#     i=i+1

#48.  wapt extract the values form the given list:
# n=eval(input("enter a list: "))
# i=0
# while i<len(n):
#     print(n[i])
#     i=i+1

#49. wapt extract from the given  string , upper case only:
# n=input("enter a value:")
# i=0
# while i<len(n):
#     if 'A'<=n[i]<='Z':
#         print(n[i])
#     i=i+1
#50 .wapt extract from the given  integer only from list :
# n=eval(input("enter a list"))
# i=0
# while i<len(n):
#     if type(n[i])==int:
#         print(n[i])
#     i=i+1
# 51. wapt extract from the given  string , lower case only:
# n=input("enter a values: ")
# i=0
# out=''
# while i<len(n):
#     if 'a'<=n[i]<='z':
#         out=out+n[i]
#     i=i+1
# print(out)


#52. WAPT  extract vowel in given string
# n=input("enter a string: ")
# i=0
# st=''
# while i<len(n):
#     if n[i] in 'AEIOUaeiou':
#         st=st+n[i]
#     i=i+1
# print(st)


#53. WAPT find the product of all float numbers , present at odd index in given tuple
# n=eval(input("enter a tuple: "))
# i=0
# out=1
# while i<len(n):
#     if type(n[i])==float and n[i]%2!=0:
#         out=out*n[i]
#     i=i+1
# print(out)

# 54. wapt extract upper and lower char, digits and special store each type sparate variable:
# n=input("enter a value: ")
# i=0
# lower=""
# upper=""
# digits=""
# specail=""
# while i<len(n):
#
#     if 'a'<=n[i]<='z':
#         lower=lower+n[i]
#     elif 'A'<= n[i]<='Z':
#         upper=upper+ n[i]
#     elif '0'<=(n[i])<='9':
#         digits=digits+n[i]
#     else:
#         specail=specail+n[i]
#     i=i+1
# print(f"lower: '{lower}' , upper: '{upper}',digits: '{digits}',specail: '{specail}'")
#

#55. wapt find the sum of intger form the given list:
# n=eval(input("enter a values: "))
# sum=0
# i=0
# while i<len(n):
#     if type(n[i])==int:
#         sum+=n[i]
#     i+=1
# print(sum)

# 56. wapt convert all lower case into upper case without using inbuilt function:
# n=input("enter a value: ")
# upper=''
# lower=''
# i=0
# while i<len(n):
#     if 'a'<=n[i]<='z':
#         upper+=chr(ord(n[i])-32)
#     elif 'A'<=n[i]<='Z':
#         lower+=chr(ord(n[i])+32)
#     else:
#         upper+=n[i]
#     i+=1
# print(upper,lower)

# ***************************************[FOR LOOP]***************************************************

#1.WAPT fetch even from 1  to 15:
# for i in range(1,16):
#     if i%2==0:
#         print(f"even number: {i}")

#2.WAPT find the length of the  collection without  using len():
# n=eval(input("enter a names: "))
# count=0
# for i in n:
#     count+=1
# print(count)

# 3.WAPT extract the vowels from the string:
# n=eval(input("Enter a data: "))
# for i in n:
#     if i in "aeiouAEIOU":
#         print(f"it's vowels: {i}")

# 4. WAPT replace empty space with '_' for given data:
# n=input("enter data: ")
# name=""
# for i in n:
#     if i==" ":
#         name+="_"
#     else:
#         name+=i
#
# print(name)

# HW 5. wapt check given string is paladinrome or not? without slicing and inbuild ():
# n=input("enter a string: ")
# if n==n:
#     print(f"it's paladinrome {n}")
# else:
#     print(f"it's not paladinrome {n}")


# 6. wap to print factorial number
# n=int(input("Enter The Number: "))
# prod=1
# for i in range (1,n+1):#n+1 facts format
#     prod=prod*i
# print(prod)

# 7. wap to print all divisor of the given number
# n=int(input("Enter The Number: "))
# print(f"divisor {n} are:")
# for i in range (1,n+1):
#     if n%i==0:
#         print(i)

# #8. WAPT get the following output
# n=(8,9.0,'love','day','gokul','reshma',[7,8])
# out={}
# for i in n:
#     if isinstance(i,str):
#         out[i]=len(i)
# print(out)


# # 9. WAPT get the following output:
# p=['abdul',87.9,'shachu',7,9+0j,'guna']
# out={}
# for i in p:
#     if type(i)==str:
#         out[i]=i[0]+i[-1]
# print(out)


#10. WAP
# n='Maple123'
# upper={}
# for i in n:
#     if 'a' <= i <= 'z':
#         upper[i]=chr(ord(i)-32)
#     elif 'A' <= i <= 'Z':
#         upper[i]= chr(ord(i)+32)
# print(upper)
#

#11. wapt a to z
# for i in range(65,91):
#     print(chr(i),end=" ")
# for i in range(ord('A'),ord('Z')):
#     print(chr(i))

# 12. wapt following output:
# n="hii baby how are you"
# out={}
# for i in (n.split()):
#         out[i]=len(i)
# print(out)
# print(n.split())# split() give sprate vau in string, its give value as list only.

# 13 wapt following output
# l=['python.py','google.com']
# out=[]
# for i in l:
#     out.append(i.split(".")[-1])
# print(out)

#14. wap for perfect number:
n=int(input("enter a number:"))
sum=0
for i in range (1,n):
    if n%i==0:
        sum=sum+i

if sum==n:
        print(f"its perfect number")
else:
        print(f"its  not perfect number")

