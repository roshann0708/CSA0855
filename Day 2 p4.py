a=[]
b=[]
x=int(input("Enter the number of elements of L1-"))
print("Enter L1 elements-")
for i in range (x):
    a.append(input(""))
y=int(input("Enter the number of elements of L2-"))
for i in range (y):
    b.append(input(""))

a=a+b
a.sort()
print(a)
