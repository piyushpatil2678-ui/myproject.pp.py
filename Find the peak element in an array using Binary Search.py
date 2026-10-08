# Find the peak element in an array using Binary Search.

def peak_element(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return arr[low]


arr = list(map(int, input("Enter numbers: ").split()))

print("Peak element:", peak_element(arr))
