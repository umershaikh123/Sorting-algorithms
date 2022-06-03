sample_list = [45, 345, 2, 4, 6, 645, 56, 65, 78, 34, 34, 34, 345, 90, 55, 23, 12, 40, 11]
# split 1 = L
# split 2 = M

def external_merge_sort(list):
    L = []
    M= []
    n = len(list)

    while len(L) == 0 or len(M) == 0:
        for i in range(n):
            
            if i == 0:
                L.append(list[i])
                split_list = True
                print("Split list 1 = " , split_list)
 
            else:
                if list[i] < list[i - 1]:
                    if split_list == True:
                        print("Split list 2 = " , split_list)
                        split_list = False

                    else:
                        split_list = True
    
                if split_list == True:
                    print("Split list 3 = " , split_list)
                    L.append(list[i])
                else:
                    print("Split list 4 = " , split_list)
                    M.append(list[i])
    
        print("L = " , L , "\n")
        print("M = " , M , "\n")
 


        list = []
        Li = 0
        Mi = 0
        if len(M) == 0:
            return L

        for i in range(len(L) + len(M)):
            if i == 0:
                if L[i] < M[i]:
                    list.append(L[Li])
                    Li  += 1
                else:
                    list.append(M[Mi])
                    Mi += 1
            else:
                if Li  == len(L):
                    list.append(M[Mi])
                    Mi += 1
                elif Mi == len(M):
                    list.append(L[Li ])
                    Li  += 1
                else:
                    if L[Li ] < M[Mi]:
                        list.append(L[Li ])
                        Li  += 1
                    else:
                        list.append(M[Mi])
                        Mi += 1        
        L = []
        M = []

print("Unsorted List:", sample_list)
print("Sorted List:", external_merge_sort(sample_list))