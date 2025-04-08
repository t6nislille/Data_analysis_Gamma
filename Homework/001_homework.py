""" Find age"""
current_year = 2023
year_of_birth = 1998

age = current_year - year_of_birth

""" Find missing code part """
code_1 = "354"
code_3 = 123

x = 152
y = 132

# Find a remainder of x divided by y
z = x % y

# Multiply the result by 13
q = z * 13

# Find the square root of the result
s = q ** 0.5

# Leave only whole part of result
w = int(float(s))

""" Save code to a separate variable"""
whole_code = code_1 + "-" + str(w) + "-" + str(code_3)

""" Print line using data from variable """
user_name = 'John'
user_surname = 'Smith'

print("Hello " + user_name + " " + user_surname + "." + " You are " + str(age) + " years old. " + "Your secret code is " + whole_code + ".")