x=input("Enter the month-")
y=int(input("Enter the date-"))

if (x=="March" and y>19)or x=="April" or x=="May" or(x=="June" and y<21):
    print("The season is currently summer")

elif (x=="June" and y>20)or x=="July" or x=="August" or (x=="September" and y<22):
    print("The season is currently Spring")

elif (x=="September" and y>21)or x=="October" or x=="November" or (x=="December" and y<21):
    print("The season is currently Fall")

else: print("The season is currently Winter")
