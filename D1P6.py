def marea(A,Len):
    a=0
    for i in range(Len):
        for j in range(i+1,Len):
            a=max(a,min(A[j],a[j])*(j-i))
    return a

n=int(input("Enter total number of array elements-"))
print("Enter array elements-")
x=[]
for i in range(n):
    x[i].append(int(input(""))
                
y=int(marea(x,n))

print(y)
