
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

n=eval(input("enter a number: "))
sum=0
for i in str(n):
    fact=1
    for j in range(1,int(i)+1):
        fact=fact*j
    sum+=fact
if sum==n:
    print("strong number")
else:
    print("not strong number")


