x=int(input("Total users-"))
y=int(input("Staff users-"))

if x==0 or y==0:
    print("Invalid input")
else:
    a=y/3
    print("Total users:",x-a-y)
