def sumDig(n):
    s=0;
    while(n!=0):
        digit = n%10
        s+=digit*digit
        n=n//10
    return s;

def ishap(n):
    s=set()
    s.add(n)
    while(True):
        if(n==1):
            return True
        n=sumDig(n)
        if n in s:
            return False
        s.add(n)
    return False

n=int(input("N="))
if(ishap(n)):
    print("True")
else:
    print("False")
