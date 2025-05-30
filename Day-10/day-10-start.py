
def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return 'Please enter valid input'
    else:
        formated_f_name =f_name.title()
        formated_l_name = l_name.title()

    return f"The formated name is : {formated_f_name} {formated_l_name}"




print( format_name(input("Type first name : "), input("Type last name : ")))


