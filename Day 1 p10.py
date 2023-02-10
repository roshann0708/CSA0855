a=input("S= ")
c=[]
for i in range (len(a)):
    t=1
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            a[j]="\0"
            t=t+1
    c.append(t)
print(c)
