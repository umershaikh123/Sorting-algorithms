# Bubble sort in Python

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(len(array) - i -1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        t = array[j]
        array[j] = array[j+1]
        array[j+1] = t



data = [-2, 45, 0, 11, -9 , 0 , 8 , 10 , -9]
bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)