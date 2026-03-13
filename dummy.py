
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
n=int(input("enter n: "))
i=1
while i<=n:
    if i%3==0 and i%5==0:
        print(i)
    i+=1

