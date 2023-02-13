n=int(input("Enter the number of elements-"))
if(n>0):
    o=0
    e=0
    for i in range(n):
        a=int(input("Enter the element-"))
        if(a%2==0):
            e=e+(a*a)
        else:
            o=o+(a*a)
    print(o,e)
else:
    print("Invalid input")
        
