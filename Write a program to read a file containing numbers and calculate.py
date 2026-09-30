# Write a program to read a file containing numbers and calculate
# sum, average, minimum, and maximum, while ignoring invalid data.

file = open("myfile.txt", "r")

numbers = []

for line in file:
    try:
        number = float(line)
        numbers.append(number)
    except ValueError:
        pass

file.close()

if len(numbers) > 0:
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    print("Sum =", total)
    print("Average =", average)
    print("Minimum =", minimum)
    print("Maximum =", maximum)
else:
    print("No valid numbers found.")
