MAX_CHARS = 256
def areiso(s1, s2):
    m=len(s1)
    n=len(s2)
    if m!= n:
        return False
    marked =[False]
    marked=[False]*MAX_CHARS
    map=[-1]*MAX_CHARS
    for i in range(n):
        if map[ord(s1[i])]==-1:
            if marked[ord(s2[i])]==True:
                return False
            marked[ord(s2[i])]=True
            map[ord(s1[i])]=s2[i]
        elif map[ord(s1[i])]!=s2[i]:
            return False
    return True

x=input("X=")
y=input("Y=")
z=areiso(x,y)

print(z)
