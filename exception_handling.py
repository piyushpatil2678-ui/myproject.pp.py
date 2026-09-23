def check_number(num):
    if num < 0:
        raise ValueError("Number cannot be negative")
    print("Number is valid")


try:
    n = int(input("Enter a number: "))
    check_number(n)

except ValueError as e:
    print("Error:", e)
