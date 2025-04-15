"""  """

string_sample = "Hello world world"
string_sample2 = "first letteR is lowErcase"
string_sample3 = " extra whitespace string "
string_sample4 = "  !!** extra whitespace string ** "

# # [start:end:step]
# print(string_sample[0])  # First letter
# print(string_sample[-1]) # Last letter
# print(string_sample[4:13]) # Letters 4-13
# print(string_sample[6:]) # From letter 6 to the end
#
# print(string_sample[::2]) # Every second character
# print(string_sample[::-1]) # From back to front


# print(string_sample.upper()) # Upper case
# print("a" > "A")  # True


# user_name = "Jack"
# db_name = "jack"
#
# print(user_name.upper() == db_name.upper()) # True

# print(string_sample2.capitalize()) # First word is capitalized
# print(string_sample2.title()) # Every First Letter Is Capitalized (e.g. names)

# print(string_sample3.strip()) # Deletes extra whitespaces in the beginning and end
# print(string_sample4.strip(" *")) # Deletes " *" from the string
# print(string_sample4.lstrip()) # Deletes from the left
# print(string_sample4.rstrip()) # Deletes from the right
#
# print(string_sample.replace("world", "planet", 1))
# print(string_sample.replace(" ", ""))
#
# print(string_sample.count("world")) # Count characters
# print(string_sample.count("world", 7)) # Start count from index 7
#
# print(string_sample.find("world")) # Index tho where the string starts

# print("123".zfill(10)) # Fill with 0-s upto limit(10)


""" Building Strings """

# print("Hello" + " " + "world", end="") # Line breaker
# print("Hello", 123 , True, sep="") # Get rid of whitespace
# print("Hello", 123 , True, sep="<>") # Replace whitespace with <>

# name = "John"
# salary = 2000
# string = "{}\'s salary is {1}. {0} is good worker."
# print(string.format(name, salary))

# p = "computer"
# pr = 1200
# string = "This {product} costs {price:.2f}"
# print(string.format(price=pr, product=p))

# name_1 = "John"
# print(f"This is {name_1}") # f is for formating

# print(r"\n") # r for raw, ignores formating

# byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
# print(byte_sting.decode('utf-8'))