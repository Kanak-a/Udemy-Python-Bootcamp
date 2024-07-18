#Average height calculator
student_height = input("Input a list of heights: ").split()
#student_height is a str containing list, we need to convert it into integer type
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])  
print(student_height)

#calculate the average of the heights
sum = 0
count = 0
for height in student_height:
    count +=1
    sum +=height
average = round(sum / count)

print(f"Average is: {average}")
    
    

