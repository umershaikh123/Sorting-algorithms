def Sort(array , n ):
    for i in range(n):

        for j in range(n-i-1):

            if(array[j+1] < array[j]):
                t = array[j]
                array[j] = array[j+1]
                array[j+1] = t
    return array

    

def SpecificSort(array , k ):
    for i in range(3):

        for j in range(3-i-1):
            
            if(array[j+1][k] < array[j][k]):
                t = array[j]
                array[j] = array[j+1]
                array[j+1] = t
    return array



A = [[9,8,5] ,[7,1,2],[4,3,6] ]
M = []

for i in range(3):
    for j in range(3):
        M.append(A[i][j])
 

M = Sort(M , len(M))

s = 0
for i in range(3):
    for j in range(3):
        A[i][j] = M[s]
        s += 1

print(A)


#for i in range(3):
#    print(Sort(A[i] , len(A)))