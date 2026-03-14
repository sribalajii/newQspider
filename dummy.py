
# n=input("enter a name: ")
# print(f"the reverse of '{n}' is : '{n[::-1]}'")
# if n==n[::-1]:
#     print(f"it's a paladinrome {n}")
# else:
#     print(f"it's not paladinrome {n}")
# x = 5
# # if x > 2:
# #     print("A")
# # if x > 4:
# #     print("B")

# n=eval(input("enter a number: "))
# sum=0
# for i in str(n):
#     fact=1
#     for j in range(1,int(i)+1):
#         fact=fact*j
#     sum+=fact
# if sum==n:
#     print("strong number")
# else:
#     print("not strong number")
# **********************************************[hackathon]***********************
# 1. dummy
# i=0
# while i<10:
#     print("i attend the class")
#     i+=1

# 2. N. natural number:
# n=int(input("number: "))
# i=1
# while i<n:
#     if i%2==0:
#         print(i,"even")
#     i+=1

# 3. to extract the number form 1 to n:
# n=int(input("number: "))
# i=1
# while i<n:
#     print(i)
#     i+=1

# 4.reverse the number from n:
# n=int(input("number: "))
# i=10
# while i>n:
#     print(i)
#     i-=1

# 5. ask password until correct:
# pd=1234
# u=int(input("pd: "))
# i=1
# while u!=pd:
#     u=int(input("pd wrong. try again: "))
# print("pd correct")

# pd=1234
# u=int(input("pd: "))
# while u!=pd:
#     u=int(input("wrong pd , try again: "))
# print("pd is correct")

# 6. wapt between 1 to n ,which are divide by 3&5:
# n=int(input("enter n: "))
# i=1
# while i<=n:
#     if i%3==0 and i%5==0:
#         print(i)
#     i+=1

# 7. fetch the number between 1 and 100 , divided by 2 and 5:
# n=100
# i=1
# while i<n:
#     if i%2==0 and i%5==0:
#         print(i)
#     i+=1

# 8. prime number:
# num=int(input("enter anum: "))
# if num==1:
#     print("it's not prime number")
# elif num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("it's not prime number")
#             break
#     else:
#             print("it's prime number")
#
# else:
#     print("it's not prime number ")

#
# n=int(input("n:"))
# if n==1:
#     print("not")
# elif n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("not")
#             break
#     else:
#         print("prime")
# n=int(input("enter a number: "))
# if n==1:
#     print(f"it's not prime number {n}")
# elif n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print(f"it's not prime number {n}")
#             break
#     else:
#         print(f"it's prime number {n}")
# else:
#     print(f"it's not prime number {n}")
# 8. 2nd table
# i=1
# while i in range(1,11):
#     print(i,"X",2,"=",i*2)
#     i+=1
# 9. reverse the order:
# n=int(input("enter num: "))
# rev=0
# i=n
# while i >0:
#     ld=i%10
#     rev=rev*10+ld
#     i=i//10
# print(rev)
# n=int(input("num: "))
# rev=0
# i=n
# while i>0:
#     ld=i%10
#     rev=rev*10+ld
#     i=i//10
# print(rev)


# 10. sum individual  digits:
# n=int(input("num: "))
# rev=0
# i=n
# while i>0:
#     ld=i%10
#     rev=rev+ld
#     i=i//10
# print(rev)
