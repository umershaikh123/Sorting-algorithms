
def matrix_Creation(Row , Column):     
    M = [] 
 
    for i in range(Row):     
        A = []           
        for j in range(Column):                 
            print("\n" ,"Enter " , j+1 , "value of Row ", i+1 , " :")
            A.append(int(input(" ")))           
        M.append(A)   
    print("\n","Matrix : "  )
    for i in range(Row):
        print("",M[i])
    return M
 


def get_pivot_element():
    r = int(input("Enter the row number of the pivot element:- "))
    c = int(input("Enter the column number of the pivot element:- "))
    return [r - 1, c - 1]


# Make pivot = 1
def P1(matrix, pr, pc):
    p = matrix[pr][pc]
    for i in range(len(matrix[pr])):
        n = matrix[pr][i]
        matrix[pr][i] = n / p

    return matrix

# make pivot column = 0
# pivot row index = pri

def Pc(matrix, pri):
    pivot_row = matrix[pri]

    for i in range(len(matrix)):
        if i != pri:
            row = matrix[i] 
            for j in range(len(row)):
                number = row[j]
                row[j] = number + number*pivot_row[j]*-1
                
    return matrix   