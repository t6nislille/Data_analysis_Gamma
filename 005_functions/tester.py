"""" Functions """
# def say_hello():  # Function that say's hello
#     print("Hello")
#
#
# say_hello()



# def say_hello(name):    # Parameter name
#     return f"f Hello {name}"
#
#
# print(say_hello("Jack")) # Argument "Jack"



# def rect_area(a: int | float, b: int | float) -> int | float:    # Parameters a, b
#     return a * b
#
#
# print(rect_area(10, 20))    # Argument 10, 20



# def print_employee_message(employee, tax_rate):
#     print(f"Hello {employee["first_name"]} {employee["last_name"]}. "
#         f"your salary before tax is {employee["salary"] * tax_rate:2f}$)"
#
#
# person = {
#     "first_name": "Jack",
#     "last_name": "Smith",
#     "salary": 2500,
# }
#
#
# print_employee_message(person, 1.24)



# def filter_adult(ages):
#     adults = []
#     for age in ages:
#         if age >= 18:
#             adults.append(age)
#         return adults
#
#
# ages = [35, 12, 8, 45, 29, 31, 18, 5]
# print(filter_adult(ages))



# def is_adult(age):
#     if age <= 0:
#         print("Wrong age!")
#         return None
#     if age >= 18:
#         return True
#     return False
#
#
# print(is_adult(54))



# def tester(a, b, c=0, *args): # Args gathers limited amount of arguments
#     print(a + b + c)
#     print(args)
#
#
#
# print(tester(1, 2, 77, 1, 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10))



# def sums_everything(*numbers: int | float) -> int | float:  # Sums unlimited amount of numbers
#     result = 0
#     for num in numbers:
#         result += num
#     return result
#
# print(sums_everything(123, 123, 84, 89))



# def tester(a, b, c=0, *args,  **kwargs):  #**kwargs stands for keyword arguments (unlimited amount)
#     print(a + b + c)
#     print(args) # Creates a list
#     print(kwargs) # Creates a dictionary
#
#
# print(tester(1, 2, 77, 1, 1, 2, 3, 4, "asdasd", True, name="jack", surname="Smith", age=45))



# a, b ,c = 1, 2, 3
#
#
# def sample():
#     a, b, c = 10, 20 ,30
#     print(a, b, c)
#
#
# sample()
# print(a, b, c)

# def sample():
#     global c # To change global variable
#     c += 100 # Global variable
#     a, b = 10, 20
#     print(a, b, c)
#
#
# sample()
# print(a, b, c)


""" Find area """
# def area(a, b):
#     return a * b
#
#
# def count_order_material(order):
#     total = 0
#     for batch in order:
#         carper_area = area(batch["width"], batch["height"])
#         total_material = carper_area * batch["amount"]
#         total += total_material
#     return total
#
#
# def print_results(order):
#     total_material = count_order_material(order)
#     print(f"Total material needed for order is {total_material} cm2")
#
#
# order = [
#     {
#         "size": "small",
#         "width": 30,
#         "height": 20,
#         "amount": 27
#      },
#     {
#         "size": "medium",
#         "width": 50,
#         "height": 40,
#         "amount": 34
#     }
# ]
#
# print_results(order)


""" Import functions """
# import my_functions
# print(my_functions.double(200))
# print(my_functions.triple(200))

# import  my_functions as helper # Import with a nickname
# print(helper.double(200))
# print(helper.triple(200))

# from my_functions import double, triple  # Import separate functions
# print(double(200))


# def wrapper(fn): # Fn short for function
#     print("Starting...")
#     fn()
#     print("Ending...")
#
#
# def say_hello(name):
#     print(f"Hello {name}!") # Function without return always returns None
#
# wrapper(lambda: say_hello("Jack")) # Lambda short way to define a function


# a = lambda a, b: a * b
# print(a(20, 30))


# def sort_method(x):
#     return x[1]
#
#
# lst = [[4, 3], [5, 2], [1, 6], [3, 1], [2, 5]]
# # lst.sort(key=sort_method) # Sorts by the second element in the list
# lst.sort(key=lambda x: x[1]) # Sorts by the second element in the list
# print(lst)























