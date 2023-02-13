def co(n,s):
    if n==0:
        return 1
    c=0
    for i in range(s,5):
        c=c+co(n-1,i)
    return c
x=int(input("Enter a number-"))
print(co(x,0))
