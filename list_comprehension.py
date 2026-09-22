# Create a list of all numbers from 1 to 100 that are divisible by both 3 and 5.
list = [i for i in range(0,101) if i%3==0 and i%5==0]
print(list)


# Create a list of squares of all even numbers between 1 and 50.
l1 = [i*i for i in range(1,51) if i%2==0]
print(l1)


# Flatten a 2D list into a 1D list using a single list comprehension.
matrix = [[1,2,3],[8,9],[6,4,2,7],[3,8,4,2]]     #    Flatten means converting a nested list into a single-level list.
l2 = [num for row in matrix for num in row]
print(l2)


# Create all possible (x, y) pairs where x and y are from 1 to 5 and x + y is even.
l3 = [(x,y) for x in range(1,6) for y in range(1,6) if (x+y)%2==0]
print(l3)


# From a list of strings, create a list containing only strings that are palindromes.
words = ["madam", "hello", "level", "python", "radar"]    # A palindrome is a word that reads the same forward and backward.
l4 = [word for word in words if word == word[::-1]]
print(l4)

# Find
l5 =[i for i in range(1,101) if i>1 and all(i%n!=0 for n in range(2,i))]
print(l5)


# Given a nested list, create a flat list containing only even numbers greater than 10.
l6 = [[3,4,2,1],[8,9,30,7],[5,6,7,8]]
lis = [i for row in l6 for i in row if i>10 and i%2==0]
print(lis)



# Given a string, create a list of characters that occur more than once.

s = (1,2,4,1,5,1,6,1,5,1)
repeated = [i for i in set(s)if s.count(i) > 1]
print(repeated)

# Given two lists, create a list containing their common elements without duplicates.
ll = [1,3,2,1,2,4,5,6]
lll = [1,5,6,8,9,9]
p = [x for x in set(ll) if x in lll]
print(p)

# Given a matrix, create a list containing its diagonal elements.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal = [matrix[i][i] for i in range(len(matrix))]

print(diagonal)

