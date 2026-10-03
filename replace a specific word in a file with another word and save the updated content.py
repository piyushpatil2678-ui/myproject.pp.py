
# Write a program to replace a specific word in a file with another word and save the updated content.
file = open("myfile.txt", "r")

lines = file.readlines()

word = input("This word: ")
new_word = input("Replace word to this: ")

found = False

for i in range(len(lines)):
    if word in lines[i]:
        lines[i] = lines[i].replace(word, new_word)
        found = True

file.close()

file = open("myfile.txt", "w")
file.writelines(lines)
file.close()

if found:
    print("Word is replaced successfully!")
else:
    print("Word not found!")
