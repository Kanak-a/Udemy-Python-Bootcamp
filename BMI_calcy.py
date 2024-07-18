#BMI caculator
name = input("Enter your name: ")
weight = input("Enter your weight = ")
height = input("Enter your height = ")
bmi = float(weight) / float(height)**2

print("BMI details for "+ name + " is : ")
print("BMI = ", int(bmi))