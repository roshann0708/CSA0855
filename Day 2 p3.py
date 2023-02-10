print("Enter three sentences-")
a=input("")
b=input("")
c=input("")

x=len(a.split())
y=len(b.split())
z=len(c.split())

if x>y and x>z:
    print(x)
elif y>z:
    print(y)
else:
    print(z)
