def merge_sort(arr):
    if len(arr)>1:
        # 1) Divide into small subproblems
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        # 2) Conquer each subproblem Recursively
        merge_sort(L)
        merge_sort(R)

        # 3) Merge routine    
        i = 0
        j = 0
        k = 0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1
if __name__ == "__main__":
    arr = [8,7,6,5,4,3,2,1]
    print("List = {}".format(arr))
    merge_sort(arr)
    print("List = {}".format(arr))

