# For range of numbers from 1 to 100
# If number divided by 3 has no remainder print number and FIZZ
# If number divided by 5 has no remainder print number and BUZZ
# If number divided by both 3 and 5 has no remainder print number and FIZZBUZZ

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, "FIZZBUZZ")
    elif num % 3 == 0:
        print(num, "FIZZ")
    elif num % 5 == 0:
        print(num, "BUZZ")