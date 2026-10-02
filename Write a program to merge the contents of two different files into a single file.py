# Write a program to merge the contents of two different files into a single file.
file_1 = open("myfile.txt","r")
l1 = []
for line in file_1:
    l1.append(line)
file_1.close()

file_2 = open("calculation.txt","r")
l2 = []
for line in file_2:
    l2.append(line)
file_2.close()

l3 = l1 + l2 

new_file = open("merge_data_of_diff_file.txt","w")
new_file.writelines(l3)
new_file.close()
print("Files merged successfully!")
