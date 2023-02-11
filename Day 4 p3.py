n=int(input("Enter the number of elemenets-"))
a=[]
print("Enter the elements-")
for i in range(n):
    a.append(int(input()))
b=[]
for i in range(n):
    c=0
    for j in range(n):
        if(a[i]>a[j] and i!=j):
            c=c+1
    b.append(c)
print(b)
