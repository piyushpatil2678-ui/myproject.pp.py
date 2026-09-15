Check whether two strings are anagrams.
"""Agar do strings mein same letters same number of times aayein, chahe unka order alag ho, to wo Anagrams hain.""" 
str1 = input("enter txt1: ")
str2 = input("enter txt2: ")

s1 = sorted(str1)
s2 = sorted(str2)

if s1 == s2:
    print("this string is anargrams")
else:
    print("this string is not anargrams")
