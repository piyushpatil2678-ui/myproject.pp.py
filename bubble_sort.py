def bubble_sort(arr):
    n = len(arr)

    order = input("enter aascending(A) OR descending(D) : ").upper()

    for i in range(n):
        for j in range(0, n-i-1):
            if order == "A" :
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

            else:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = list(map(int,input("enter your list : ").split()))
print(bubble_sort(arr))
