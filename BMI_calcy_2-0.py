#BMI calculator 2.0 

name = input("Enter your name: ")
weight = input("Enter your weight = ")
height = input("Enter your height = ")
bmi = float(weight) / float(height)**2

print("BMI details for "+ name + " is : ")
print("BMI = ", int(bmi))

#the upgraded version 
if bmi < 18.5:
    print("You seem to be underweight. Gotta follow a healthy diet")
    
elif bmi>=18.5 and bmi<25:
    print("You have a normal weight. That's very good!")

elif bmi>=25 and bmi<30:
    print("You seem to be overweight. Exercise and diet is a must.")
    
elif bmi>30 and bmi<35:
    print("You are obese, keep your gym subscription ready!")
    
else:
    print("You are clinically obese, you must see a Doc.")