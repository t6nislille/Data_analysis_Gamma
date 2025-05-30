""" Error handling """
# while True:
#     try:
#         number = float(input("Enter number: "))
#     except:
#         print("The value entered is not numeric!")
#     else:
#         print(number)
#     finally:
#         print("One more time!")



# while True:
#     try:
#         number = float(input("Enter number: "))
#     except:
#         print("The value entered is not numeric!")
#         continue # Stops the cycle and starts over from the beginning
#     print(number)
#     break



# for letter in "python":
#         if letter == "h":
#             continue  # Stops the current iteration of the cycle and takes the next possible character
#         if letter == "o":
#             break  # Quits the cycle
#         print(letter) # Prints p y t



# while True:
#     try:
#         user_id = input("Please enter Estonian national id: ")
#         int(user_id)
#         if len(user_id) != 11:
#             raise Exception
#     except ValueError:
#         print("Code you entered is not numeric!")
#         continue
#     except Exception:
#         if len(user_id) > 11:
#             print("TOO LONG")
#         else:
#             print("TOO SHORT")
#         continue
#     print(user_id, "CORRECT")
#     break



""" ZIP """
# a = [1, 2, 3]
# b = ["a", "b", "c"]
#
# # zipped = list(zip(a, b))
# zipped = zip(a, b)
#
# for pair in zipped:
#     print(pair)



# a = [1, 2, 3]
# b = ["a", "b", "c"]
#
# zipped = list(zip(a, b))
# print(zipped)
# nums, letters = zip(*zipped) # Unzip
# print(nums)
# print(letters)



# x = [1, 2, 3, 4, 5, 6]
# print(*x)
# first, *rest, last = x
# print(first, rest, last)



""" FILTER """
# def filter_evens(numbers):
#     evens = []
#     for num in numbers:
#         if num % 2 == 0:
#             evens.append(num)
#     return evens
#
#
# print(filter_evens([1, 2, 3, 4, 5, 6, 7, 8]))



# nums = [123, 432, 333, 350, 6744, 9853, 6969]
#
# def filter_even(num):
#     if num % 2 == 0:
#         return True
#     return False
#
#
# # even_numbers = filter(filter_even, nums)
# even_numbers = filter(lambda num: num % 2 == 0, nums)
# print(even_numbers)
# print(list(even_numbers))



# people = [
#     {
#         "name": "Jack",
#         "surname": "Smith",
#         "age": 17
#     },
#     {
#         "name": "Sarah",
#         "surname": "Gold",
#         "age": 25
#     },
#     {
#         "name": "Bob",
#         "surname": "Summers",
#         "age": 45
#     },
#     {
#         "name": "Mary",
#         "surname": "Green",
#         "age": 15
#     }
# ]
#
# filtered_people = filter(lambda  person: person["age"] >= 18, people)
# print(list(filtered_people))



""" MAP """
# numbers = [1, 2, 3, 4, 5, 6, 7]
# squares = list(map(lambda num: num ** 2, numbers))
#
# print(squares)



# cities = ["london", "tallinn", "berlin", "paris", "riga", "helsinki"]
#
# upper_cities = list(map(str.title, cities))
# print(upper_cities)



# text = "hello world"
# # print(text.title())
# print(str.title(text))



# people = [
#     {
#         "name": "Jack",
#         "surname": "Smith",
#         "age": 17
#     },
#     {
#         "name": "Sarah",
#         "surname": "Gold",
#         "age": 25
#     },
#     {
#         "name": "Bob",
#         "surname": "Summers",
#         "age": 45
#     },
#     {
#         "name": "Mary",
#         "surname": "Green",
#         "age": 15
#     }
# ]
#
# modded_people = list(map(lambda person: {f"{person["name"]} {person["surname"]}": person["age"]}, people))
# print(modded_people)



# a = [1, 2, 3]
# b = [4, 5, 6]
#
# multiplied = list(map(lambda x, y: x * y, a, b))
# print(multiplied)



""" List comprehension """
# numbers = [1, 2, 3, 4, 5, 6 ,7]
# squares = [num ** 2 for num in numbers]
# print(squares)
#
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)
#
# labels = [f"{num} even" if num % 2 == 0 else f"{num} odd" for num in numbers]
# print(labels)



# x = [1, 2, 3]
# y = ["a", "b", "c"]
# pairs = [(a, b) for a in x for b in y]
# print(pairs)
#
# p = []   # Analog for the previous nested for loop
# for a in x:
#     for b in y:
#         p.append((a, b))
# print(p)


# numbers = [1, 2, 3, 4, 5, 6 ,7]
#
# def square(num):
#     return num ** 2
#
# squared = [square(n) for n in numbers]
# print(squared)


# numbers = [1, 2, 3, 4, 5, 6 ,7]
# squared_dict = {num: num ** 2 for num in numbers}
# print(squared_dict)
#
#
# numbers = [1, 2, 3, 4, 5, 6 ,7, 7, 8, 4]
# unique_squares = {num ** 2 for num in numbers}
# print(unique_squares)




