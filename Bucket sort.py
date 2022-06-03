# Bucket Sort in Python


def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])
    print("Bucket " , bucket , "\n")

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    print("Bucket " , bucket , "\n")

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    print("Bucket " , bucket , "\n")

    a = []
    # Get the sorted elements
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            if(bucket[i] != None ):
                a.append(bucket[i][j])
 
    return a


array = [.42, .32, .33, .52, .37, .47, .51]
arr = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
print("Sorted Array in descending order is")
a = bucketSort(arr)
print(a)





#     k = 0
#    for i in range(len(array)):
#        for j in range(len(bucket[i])):
#            array[k] = bucket[i][j]
#            print("Bucket sortin " , array , "\n")            
#            k += 1