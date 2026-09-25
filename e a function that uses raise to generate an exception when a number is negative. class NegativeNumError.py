
# Write a function that uses raise to generate an exception when a number is negative.
class NegativeNumError(Exception):
    pass
n = int(input("enter a num: "))
try:
    if n < 0 :
        raise NegativeNumError("this num. is negative ")
    else:
        print("your num is positive")
except NegativeNumError as n:
    print("warning: ",n)
