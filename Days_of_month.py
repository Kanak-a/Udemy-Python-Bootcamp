#Interactive coding exercise - days of the month

def leap_year (year):
    if year % 4 == 0:
        if year %100 == 0:
            if year %400 == 0:
                return True
            else :
                return False
        else:
            return True
    else:
        return False

def days_of_month(year, month):
                 #jan feb mar apr may jun jul aug sep oct nov dec
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year) == True :
        #then check if month is february month = 2
        if month == 2:
            days = month_days[month - 1] + 1
            
    return month_days[month - 1]
            
    #OR 
    """
    if leap_year(year) and month == 2:
        return 29 
    """
        
    return days

#main
year = int(input("Enter a year: "))
month = int(input("Enter the month: "))
days = days_of_month(year, month)
print(days)
        
