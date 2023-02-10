s=input("s= ")
t=input("t=")
k=ord(s[0])-ord(t[0])
print(k)
l=0
if len(s)==len(t):
    for i in range(1,len(s)):
        if((ord(s[i])-ord(t[i]))==k):
            l=l+1
    if(l==(len(s)-1)):
       print("TRUE")
    else:
        print("FALSE")
else:
    print("FALSE")

            
