#functions with output 
#a function which changes the input names into title case

def format_name(f_name, l_name):
    """ Take the first and the last name and format it 
    to return the title case version of the name. """
    
    f_name_lower = f_name.lower()
    l_name_lower = l_name.lower()
    name_capital = f_name_lower.capitalize()
    surname_capital = l_name_lower.capitalize()
    return f"Name : {name_capital} {surname_capital}"
    
    
    

#main -
f_name = input("What's yourr first name: ")
l_name = input("What's your last name: ")
print("Formatted name and last name looks like - ")
formatted_string = format_name(f_name, l_name)
print(formatted_string)

