# Selection sort

# Selection sort is a sorting algorithm that selects the smallest element
# from an unsorted list in each iteration and places that element at the beginning of the unsorted list.






def selectionSort(array, size):
   
    for i in range(size):
        min_idx = i

        for j in range(i + 1, size):
         
            # to sort in descending order, change > to < in this line
            
            if array[j] < array[min_idx]:
                min_idx = j
         
       
        (array[i], array[min_idx]) = (array[min_idx], array[i])




data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print("\n", 'Sorted Array in Ascending Order: ' , "\n")
print(data , "\n")