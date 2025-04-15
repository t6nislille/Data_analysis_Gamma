"""" For cycle """
# print(list(range(10))) # Create a list of numbers
# print(list(range(100, 200, 10))) # List of numbers from 100 to 200 with steps of 10

# for num in range(100): # Range in for loop
#     print(num)

# a = [1, 2, 3, 4, 5 ,6]
# b = ["A", "B", "C", "D", "E", "F"]

# for index in range(len(a)):
#     print(a[index], b[index])

# for num in a:
#     for letter in b:
#         print(num, letter)

# for num1 in range(10): # Loops 10 times
#     for num2 in range(10): # Loops 10  * 10 = 100
#         for num3 in range(10): # Loops 10 * 10 * 10 = 1000
#             print(num1, num2, num3)

# for num in range(10):
#     print(num)
#
# print("NUM", num)



# people = [
#     ("Jack", "Smith", 2000, "m"),
#     ("Sarah", "Gold", 2500, "f"),
#     ("Bob", "Summer", 3000, "m"),
#     ("Jane", "Green", 5000, "f"),
# ]
#
# for first_name, last_name, salary, gender in people:
#     if gender == "m":
#         print(f"This is {first_name} {last_name}. His salary is {salary:.2f}$")
#     elif gender == "f":
#         print(f"This is {first_name} {last_name}. Her salary is {salary:.2f}$")
#
# #Another way to do it
# for first_name, last_name, salary, gender in people:
#     gender_pronounce = ""
#     if gender == "m":
#         gender_pronounce = "his"
#     elif gender == "f":
#         gender_pronounce = "her"
#     print(f"This is {first_name} {last_name}. {gender_pronounce.title()} salary is {salary:.2f}$")



# All conditions are used when "if" is used
# x = 100
# if x > 0:
#     print("X is positive")
# if x < 50:
#     print("X is half way to a 100")
# if x == 100:
#     print("X is 100")



# idcode = "39508250830"

# if len(idcode) == 11 and idcode.isdecimal():
#     print(idcode, "Correct!")
# else:
#     if len(idcode) > 11:
#         print("Code is too long!")
#     elif len(idcode) < 11:
#         print("Code is too short!")
#     if not idcode.isdecimal():
#         print("Code is not all numeric!")


# if len(idcode) == 11 and idcode.isdecimal():
#         print(idcode, "Correct!")
# elif len(idcode) > 11:
#     print("Code is too long!")
# elif len(idcode) < 11:
#     print("Code is too short!")
# else:
#     print("Code is not all numeric!")


# if len(idcode) == 11:
#     if idcode.isdecimal():
#         print(idcode, "Correct!")
#     else:
#         print("Code is not correct!")
# elif len(idcode) > 11:
#     print("Code is too long!")
# else:
#     print("Code is too short!")



# name = input("Enter name: ")
# if name:
#     print(f"Hello {name.title()}!")
# else:
#     print("Hello stranger!")


# # FizzBuzz
# # For range of numbers from 1 to 100
# # If number divided by 3 has no remainder print number and FIZZ
# # If number divided by 5 has no remainder print number and BUZZ
# # If number divided by both 3 and 5 has no remainder print number and FIZZBUZZ
#
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num, "FIZZBUZZ")
#     elif num % 3 == 0:
#         print(num, "FIZZ")
#     elif num % 5 == 0:
#         print(num, "BUZZ")



"""" Dictionaries """
# empty = {} # Create empty dictionary
# empty = dict() # Convert or create a dictionary

# random_dict = {
#     "first_name": "Jack",
#     1: "integer key", # 1 and 0 converts to bool, 1 True and 0 False
#     0.42: "float key",
#     (1, 2, 3): "tuple key",
#     True: "bool key",
# }
#
# print(random_dict[1])



# person = {
#     "first_name": "Jack",
#     "Last_name": "Smith",
#     "information": {
#         "eye_color": "blue",
#         "height": 186,
#         "weight": 100,
#     },
#     "clothes": [
#         "jeans",
#         "t-shirt",
#         "jacket",
#         "shoes",
#     ]
# }
#
# # print(person.get("first_names", False)) # Override key error so the program won't stop
# # print(person.get("first_name")) # Get info from dictionary
# # print(person.get("information").get("eye_color")) # Get info from nested dictionary
# # print(person["clothes"][2])



# person = {
#     "first_name": "Jack",
#     "last_name": "Smith",
# }
#
# person["first_name"] = "Bob" # Change key's in dictionary
# person["phone"] = "555-555-555" # If key doesn't exist, it adds it
# person.update({"phone": "444-444-444", "salary": 2000}) # If key doesn't exist, it adds it, if key exists then no duplicates are allowed
# # del person["phone"] # Delete from dictionary
# # print(person.pop("salary")) # Returns from the dictionary
# # print(person.popitem()) # Returns last item added to dictionary




# # Create key with for loop
# x = {}
# for num in range(100):
#     x[num] = num **2
#
# print(x)


# # Copy dictionary
# my_car = {
#     "make": "BMW",
#     "model": "320",
#     "info": {
#         "color": "white",
#         "mileage": 12000,
#     }
# }
#
# my_other_car = my_car.copy()  # Copy dictionary
# print(my_other_car)



# person = {
#     "first_name": "Jack",
#     "last_name": "Smith",
#     "age": 18,
# }
# # # For loop iterates through keys not data
# # for x in person:
# #     print(x)
#
# print(person.keys())
# print(person.values())
# print(person.items())
#
# for x in person.values(): # Iterate through dictionary values
#     print(x)
#
# if "Jack" in person.values():
#     print("YES")

# x = [("one", 1), ("two", 2)]
# print(dict(x)) # Convert list to dictionary