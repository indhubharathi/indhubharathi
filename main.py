#write a program that determines whether a year entered by the user is leap year or not using if-elif-else statements
input_year = int(input("Enter the Year to be checked: "))
if(input_year%4 == 0):
    if(input_year%100 == 0):
        if(input_year%400 == 0):
            print("%d is Leap Year" %input_year)
        else:
            print("%d is Not the Leap Year" %input_year)
    else:
        print("%d is Leap Year" %input_year)
else:
    print("%d is Not the Leap Year" %input_year)