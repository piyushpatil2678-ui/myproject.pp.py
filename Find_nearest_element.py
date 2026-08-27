# Find the nearest element to a given number.
def nearest_element(num):
    min_diff = 100
    nearest = arr[0]

    for i in range(len(arr)):
        if abs(arr[i] - num) < min_diff:
            min_diff = abs(arr[i] - num)
            nearest = arr[i]

    return nearest

arr = list(map(int, input("enter elements: ").split()))
num = int(input("our target: "))

print(arr)
print(nearest_element(num))
