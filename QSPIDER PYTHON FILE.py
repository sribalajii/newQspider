# 1. add two numbers
# a=int(input("enter the number : "))
# b=int(input("enter the number : "))
# print(a+b)
# print(f"the total value is {a+b}")
from importlib.metadata import pass_none

# 2. WAPTF the square of the number:
# c=int(input("enter the number : "))
# print(f"the square of the {c} is: {c**2}")

# 3. WAPT change float to integer number:
# d=float(input("enter a number: "))
# e=int(d)
# print(e,type(e))

# 4. WAPT print the last char form string:
# f=input(" enter a name: ")
# print(f" the last char of {f} is : {f[-1]}")

# 5. WAPT reverse the string:
# g=input("enter name: ")
# print(f"the reverse of '{g}' is : {g[::-1]}")


# 6. WAPT fetch middle value from list:
# h=eval(input("enter value: "))
# print([len(h)//2])

# 7. WAPT  extarct last number from value:
# i=(input("enter number: "))
# print(f"the last value of {i} is  : {i[-1]}")
# **************************************[IF]********************************************************
# 8. WAPT simple if program
# j=int(input("enter a number : "))
# if j%2==0:
#     print(f"{j} is even number ")

# 9.WAPT CHECK THE given string is exactly 5 char or not?:
# k=input("enter the  string: ")
# if len(k)==5:
#     print(f"'{k}' is a five char")

# 10. WAP to check the given number is greater than 200 or not?
# m=int(input("enter the number: "))
# if m>200:
#     print(f"'{m}' is greater then 200.")

# 11. WAP to print the square of the number , if it's the multiple of 3 only:
# n=int(input("enter the  number: "))
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
# o = input("enter a char: ")
#
# if 'A' <= o <= 'Z':
#     print(f"{o} is lower case")
# else:
#     print(f"{o} is not lower case")

# 14. WAP to find enter number is 3 digit number or not

# z=int(input("enter a number: "))
# if 99<=z<=999:
#      print(f"the enter  number is '{z}' is 3 digit")

# *********************************[IF-ELSE]****************************************

# 15.WAPT find enter number float number or not: note , if want check the type of data means,use TYPE()
# x=eval(input("enter a value: "))
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
# r=input("enter a values: ")
# if r[::]==r[::-1]:
#     print(f"enter name '{r}' is palaindrome")
# else:
#     print(f"'{r}'not a palaindrome ")

#18. WAPT check thee given char is vowel or not:
# s=input("enter a char: ")
# if s in ['a','e','i','o','u','A','E','I','O','U']:
#     print(f" the enter char '{s}' is vowel")
# else:
#     print(f" the enter char '{s}' not vowel")

#19. WAPT the enter value is single value datatype or multi value data type
#
# i=eval(input("enter a values: "))
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
user=input("enter your  user name: ")
if user=="balaji":
    password = input("enter your password:")
    if password=="1234":
        print("your entering successfully")
    else:
        print("enter password is wrong")
else:
    print("wrong user name")