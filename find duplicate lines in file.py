file = open("myfile.txt", "r")

lines = file.readlines()

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        if lines[i] == lines[j]:
            print(lines[i])

file.close()
