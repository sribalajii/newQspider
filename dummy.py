
n=input("enter a name: ")
print(f"the reverse of '{n}' is : '{n[::-1]}'")
if n==n[::-1]:
    print(f"it's a paladinrome {n}")
else:
    print(f"it's not paladinrome {n}")
