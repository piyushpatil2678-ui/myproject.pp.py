# Write a program to search for a particular word in a file and display the line numbers where it occurs.
file = open("myfile.txt","r")
lines = file.readlines()
word = input("find this character in the file : ")

found = False
for i in range(len(lines)):

    if word in lines[i]:
        print("the word is found at line num. ",i+1)
        found=True
if found==False:
    print("this word are not in file !")

file.close()
