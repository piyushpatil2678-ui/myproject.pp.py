# Find the second largest element.
def second_largest_ele(arr):
    current_largest = arr[0]
    second_largest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > current_largest:
            second_largest = current_largest
            current_largest = arr[i]

        elif arr[i] > second_largest and arr[i] != current_largest:
            second_largest = arr[i]

    return second_largest


arr = list(map(int, input("Enter elements: ").split()))

print(second_largest_ele(arr))
