# My First Python Script!
# This script was written when I was just starting to learn Python.
# It asks the user for some numbers and then prints out the total and average.

print("Welcome to my beginner script!")

name = input("What's your name? ")
print("Nice to meet you, " + name + "!")

numbers = []

for i in range(5):
    num = input("Enter a number: ")
    # try to convert the input to an integer
    numbers.append(int(num))

# Calculate the total
my_total = 0
for n in numbers:
    my_total = my_total + n

# Calculate the average
my_average = my_total / len(numbers)

print("You typed:", numbers)
print("Total:", my_total)
print("Average:", my_average)
