# Input string of numbers separated by '+'
input_string = input()

# Extract unique numbers from the input string
numbers = [int(num) for num in input_string.split('+')]

# Sort the unique numbers
sorted_numbers = sorted(numbers)

# Filter and join the numbers less than or equal to 3 as a string
sorted_string = '+'.join([str(num) for num in sorted_numbers if num <= 3])
print(sorted_numbers)