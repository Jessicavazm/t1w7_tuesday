# Calculate the sum of a list

# numbers = [1,2,3,4,5]

# Initialise sum to zero
# sum = 0

# Start FOR loop
# for number in numbers:
#     sum = sum + number
# print(sum)    

# Calculate the max number in a list

numbers = [1,5,34,2,67,34]
# Setting max number to first number in the list using index
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)    