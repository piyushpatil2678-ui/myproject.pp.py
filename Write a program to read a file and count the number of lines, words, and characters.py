# Write a program to read a file and count the number of lines, words, and characters without using split().
file = open("myfile.txt", "r")

lines = 0
words = 0
characters = 0
in_word = False

for line in file:
    lines += 1

    for ch in line:
        characters += 1

        if ch != " " and ch != "\n" and ch != "\t":
            if not in_word:
                words += 1
                in_word = True
        else:
            in_word = False

file.close()
print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", characters)
