def find_minimum(arr):
    minimum = arr[0]
    for element in arr:
        if element < minimum:
            minimum = element
    return minimum

print(find_minimum([0,3,-4,5,1]))

def find_middle(arr):
    summ = 0
    for element in arr:
        summ += element
    count = len(arr)
    return summ / count
print(find_middle([1,2]))
