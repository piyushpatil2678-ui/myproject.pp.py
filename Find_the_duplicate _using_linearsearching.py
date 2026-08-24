# Find the duplicate element in an array using linear searching 
                # for both single and multiple duplicate value
def duplicates(array):
    result = []
    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]==array[j]:
                result.append(array[i])
    return result

array = [32,43,21,21,32,43,54,55,2]
print(duplicates(array))        
