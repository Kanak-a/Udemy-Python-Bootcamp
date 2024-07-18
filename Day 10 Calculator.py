#day - 10 for calculator in python 
#calculator ascii art - 
#from Day10_asciiart import art
def add(num1, num2):
    result = num1 + num2
    return result

def sub(num1, num2):
    result = num1 - num2
    return result

def pro(num1, num2):
    result = num1 * num2
    return result

def div(num1, num2):
    result = num1 / num2
    return result
    
#main 
#a dictionary 
dict_op = {
    "+" : add,
    "-" : sub,
    "*" : pro,
    "/" : div
    }

num1 = int(input("Enter the first number: "))

for operator in dict_op:
    print(operator)     #will print only the keys 

operation = input("Pick an operation : ")

num2 = int(input("Enter the second number: "))

if operation in dict_op:
    calculated_function_1 = dict_op[operation]
    result = calculated_function_1(num1, num2)

    print(f"{num1} {operation} {num2} = {result}")
else :
    print("Invlaid operation ")
choice = input(f"-- Type 'y' to continue calculating from {result}  --")
loop = True
while loop:
    if choice == 'y':
        operation = input("Pick an operation : ")
        num3 = int(input("Enter the number: "))
        calculated_function = dict_op[operation]
        result_1 = calculated_function(result, num3)  
        print(f"{result} {operation} {num3} = {result_1}")
        choice = input(f"Type 'y' to continue calculating from {result_1} : ")
        

    else:
        print("Thanks for using our calcy!")
        loop = False

print("You are welcomed to use it again! Till then see ya!")