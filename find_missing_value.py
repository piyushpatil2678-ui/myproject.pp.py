# Find the missing number from 1 to n.
def find_missing_value(arr,n):
    expected_total_sum = (n*(n+1))/2
    actual_sum = 0
    for i in arr:
        actual_sum += i 

    missing_value = expected_total_sum - actual_sum
    print(missing_value)

arr = [1,2,3,4,5,6,7,9]
n = 9
find_missing_value(arr,n) 
