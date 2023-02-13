x=int(input("Enter year-"))
if x%400==0:
    print("Its a leap year")
elif x%100==0:
    print("Its not a leap year")
    print("Leap year:", x-4)
elif x%4==0:
    print("Its a leap year")
else:
    print("Its not a leap year")
    a=x%4
    print("Leap year:",x-a)
