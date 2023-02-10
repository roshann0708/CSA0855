t=int(input("Value of t="))
print("E[] =")
a=[]
b=[]
c=[]

for i in range (0,t):
    a.append(int(input("")))

print("L[] =")

for i in range (0,t):
    b.append(int(input("")))

for i in range (0,t):
    c.append(a[i]+b[i])

x=0
for i in range (0,t):
   if(x<c[i]):
       x=c[i]
print("MAXIMUM IS ",x)
