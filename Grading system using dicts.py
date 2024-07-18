#Grading system using dictionary
print("This is the grading system! \nInput your marks and get to know your grades! ")
#dictionary containing the student scores
student_scores = {
    "Harsh": 56,
    "Parth": 79,
    "Durvesh": 81,
    "Atharva": 94,
    "Yash": 85
}

#dictionary containing the student grades
student_grade = {}  #empty dcitionary
#check for the scores and refer the criteria 
"""
91 - 100 : "outstanding" 
81 - 90 : "Exceeds expectations
71 - 80 : Acceptable
< 70 : Fail"""
#looping through the student_scores 
for score in student_scores:
    if student_scores[score] < 70:
        #add the reviewed value in the another dictionary
        student_grade[score] = "Fail"
        
    elif student_scores[score] >70 and student_scores[score] <80:
        student_grade[score] = "Acceptable"
        
    elif student_scores[score] > 80 and student_scores[score] < 90:
        student_grade[score] = "Exceeds Expectations!"
        
    elif student_scores[score] >90 and student_scores[score] < 100:
        student_grade[score] = "Outstanding!!!"

print("The student grades are : ", student_grade)
print("Thanyou for using our system!")
