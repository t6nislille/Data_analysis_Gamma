# Return "Hero" from given string
example_string = "Hello bro"
print(example_string[:2] + example_string[7:])

# Return "Jack is my name" from example
example_string2 = "jack Is My NAME"
print(example_string2.capitalize())

#Return "Get rid of junk please" from example
example_string3 = "%-*Get rid of *junk* please*-L%*"
print(example_string3.strip("%-*L").replace("*", " "))

# Find all occurrences of “Estonia” in a given string ignoring the case.
example_string5 = "Welcome to estonia. Estonia is awesome, isn't it? I moved to ESTONIA 5 years ago."
print(example_string5.lower().count("estonia"))

# Write a code to return f-string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"

print(f"{var2.capitalize()}, {var3.lower()} {var1.capitalize()}")

# # Write a code to return byte_string text value
byte_string = b"\316\273"
print(byte_string.decode("utf-8"))