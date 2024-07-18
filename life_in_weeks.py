"""
Article by Tim Urban - Your life in weeks 
Create a program using math and f-string that tells us how many days 
weeks and months we have left to live until the age 90.
"""
age = int(input("Enter your age : "))
age_dif = 90 - age
days = 365
weeks = 52
months = 12
days*=age_dif
weeks*=age_dif
months*=age_dif
print(f"Your life left to live is about {days} days, {weeks} weeks, {months} months.")
print("So little time is left, hope you live them with utmost care and love!")