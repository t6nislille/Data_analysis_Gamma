""" Lists """

# empty = [] # List (list)
# empty = list()
# print(type(empty)) # Class 'list'
# print(bool(empty)) # False

# not_empty = [123, 0.32, False, None, "Hello world", [1, 2, 3, [4, 5, 6], 7, 8], False] # Different data types in a list
# print(len(not_empty))  # How many items in a list
# print(not_empty[5]) # Returns fifth item from the list
# print(not_empty[5][3]) # Return third item from fifth list
# print(not_empty[5][3][1]) # Return first item from...
# print(not_empty[2:6])


# a, b, *c = [1, 2, 3, 4] # * adds the extra number to c
#
# print("A", a)
# print("B", b)
# print("C", c)


# courses = ["Math", "Art", "English", "Programming", "History"]
#
# courses[0] = "Physics" # Change []index value in list
# # courses[0:2] = ["Math"] # Replace the first strings with a new string
# courses[0:2] = ["Math", "Estonian"]
# print(courses)

# print(list("Hello world")) # Converts the string to a list as characters


""" List Methods"""

# courses = ["Math", "Art", "English", "Programming", "History"]

# courses.append("Physics") # Modifying existing list, ads element as the last index
# courses.insert(0, "Music") # Inserts new element to a specific index
# courses.extend(["Music", "Science"]) # Add multiple elements to a list
# print(courses)

# print([1, 2, 3] + [4, 5, 6]) # Add lists together
# print([1, 2, 3] * 5) # Multiply list by index

# courses.remove("Art") # Removes element from the list (case-sensitive)
# courses.pop() # Deletes the last element in the list
# deleted = courses.pop(0) # Deletes element from the list
# print(courses)
# print(deleted)

# courses.reverse() # Reverses a list
# print(courses[::-1]) # Also reverses a list
# courses.sort() # Sorts list alphabetically (case-sensitive)
# courses.sort(reverse=True) # Reverses list alphabetically
# print(sorted(courses, reverse=True))
# print(courses)

# courses = ["Math", "Art", "English", "Programming", "History", "Physics", "art", "123", "45", "234"]

# print(courses.count("Art")) # Counts indexes in list (case-sensitive)
# print(courses.index("Art")) # Finds the index


# text = " These          words will be splitted to a list soon!"
# lst = text.split() # Splits elements to a list (excluding white-space)
# lst = text.split(", ") # Add a seperator
# print(lst)
# new_text = "***".join(lst) # Separate elements in list with ***
# print(new_text)


# a = 5
# b = a
# a += 5
# print("A", a)
# print("B", b)

# a = "Hello"
# b = a
# a += " World"
# print("A", a)
# print("B", b)

# a = [1, 2, 3, 4]
# print(id(a))
# b = a.copy() # For copying lists
# print(id(b))
# a.append(0)
# b.append(5)
# print("A", a)
# print("B", b)


# lst = [1, 2, 3, 4, 5, 6, 7]
# print(sum(lst)) # Sums up the values (doesn't count strings)
# lst = ["Atr", "Math", "Physics", "123", "art"]
# print(min(lst)) # Returns min value (returns strings also)
# print(max(lst)) # Returns max value (returns strings also)


# x = [1, 2, 3]
# x.clear() # Deletes everything from the list
# print(x)