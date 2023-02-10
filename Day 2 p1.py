x=int(input("Enter the number of steps -"))
a=1
b=2
if x==1:
    print("1")
elif x==2:
    print("2")
else:
    for i in range (x-2):
        c=a+b
        a=b
        b=c
print(c)
