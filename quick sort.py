# There are different variations of quicksort 
# where the pivot element is selected from different positions.
#  Here, we will be selecting the rightmost element of the array as the pivot element.

# pivoit number = left side per less than values or right side greater than pivot values







 

 
def partition(array, low, high):

 
  pivot = array[high]
  i = low - 1
 
  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      (array[i], array[j]) = (array[j], array[i])

 
  (array[i + 1], array[high]) = (array[high], array[i + 1])

 
  return i + 1







 
def quickSort(array, low, high):
  if low < high:


    pi = partition(array, low, high)

 
    quickSort(array, low, pi - 1)
 
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)