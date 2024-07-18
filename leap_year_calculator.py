'''
Leap year calculator 
'''
year = int(input("Enter the year: "))
#if year is evenly divisible by 4
if year % 4 == 0:
    if year % 100 == 0:
        if year%400 == 0:
            print("Year is leap")
        else:
            print("Year is not leap")
    else:
        print("Year is leap")
    
else:
    print("Given year is not a LEAP YEAR, try another one.")