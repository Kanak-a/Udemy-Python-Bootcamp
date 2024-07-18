#dictionary 101 
#printing a dictionary 
"""dict = {"01": "Kanaka", "02": "Parth", "03": "Isha"}
print("The dictionary looks like: ", dict)"""

#the correct way of writing a dictionary is --
roll_call_dict = {
        '01': 'Kanaka',
        '02': 'Parth', 
        '03': 'Arvik',
        '04': 'Kiara'
}
#printing the programming dictionary
#print("Printing the dictionary - : ", roll_call_dict )

#Adding new items  to the dictionary
roll_call_dict["05"] = "Laila"
#print("New addition: ", roll_call_dict)
#printing a particular value by passing the key 

#print(f"Roll number 3rd is: {roll_call_dict['03']}")

"""#printing an empty dictionary 
roll_call_dict = {}
print("The programming dict data is erased - ", roll_call_dict)"""

#editing a value in the dictionary 
roll_call_dict['02'] = 'Priya'
#print("Edited roll dictionary: ", roll_call_dict)

#loop through the dictionary
for roll_no in roll_call_dict:
    print(roll_no)



