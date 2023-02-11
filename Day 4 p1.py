x=int(input("Enter a number-"))
y=[]
for i in range (1,x+1):
    if i%5==0 and i%3==0:
        y.append("FizzBuzz")
    elif i%5==0:
        y.append("Buzz")
    elif i%3==0:
        y.append("Fizz")
    else:
        y.append(i)
print(y)
