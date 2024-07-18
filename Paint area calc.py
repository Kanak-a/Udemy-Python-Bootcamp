# Paint area calculator
"""1 CAN OF PAINT COVERS 5 METERS OF WALL"""
#height -> parameter and test_h ->argument
def pain_calc(height, width, cover):
    return ( height * width )/ cover
    
    
test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5   #given
no_of_can = round(pain_calc(height = test_h, width = test_w, cover = coverage))
print(f"You'll need {no_of_can} cans of paint.")