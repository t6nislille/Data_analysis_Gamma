# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number
def get_squares(lst: list[int]) -> list[int]:
    return [num ** 2 for num in lst]


print(get_squares([2, 4, 6]))


# Write a function that accepts a list of numbers
# And returns a tuple with two numbers, amount of odd and even numbers
# Example: input -> [1, 2, 3, 4, 5] output (3, 2)
# Where 3 is amount of Odds and 2 is amount of evens
def get_tuples(lst):
    odd_count = 0
    even_count = 0
    for num in lst:
        if num %2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count


print(get_tuples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# Write a function that accepts a list of numbers
# and returns largest number
def get_largest(lst: list[int | float]) -> int | float:
    return max(lst)


print(get_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



# Write a function that accepts a start number and end number
# Create a FizzBuzz for given range
# (If number divided by 3 has no remainder, print number + FIZZ
# If number divided by 5 has no remainder, print number + BUZZ
# If number divided by 5 and 3 has no remainder, print number + FIZZBUZZ)
def start_and_end(start: int, end: int):
    for num in range(start, end + 1):  # Add +1 because the last number of the range is not included
        if num %5 == 0 and num %3 == 0:
            print(num, "FIZZBUZZ")
        elif num %3 == 0:
            print(num, "FIZZ")
        elif num%5 == 0:
            print(num, "BUZZ")


start_and_end(1, 100)


# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number
def square_list():
    numbers = input("Please enter some numbers, use " " as a seperator: ").split()
    squares = []
    for num in numbers:
        squares.append(int(num) ** 2)
    return squares


print(square_list())
