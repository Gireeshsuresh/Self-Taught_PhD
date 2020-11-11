
def insertion_sort(input_array, mode):
    """
    Given an Array as input, perform Insertion Sort on the given array
    """
    for i in range(1, len(input_array)):
        key = input_array[i]
        j = i-1

        if mode =='Descending':
            while j>=0 and (key > input_array[j]):
                input_array[j+1] = input_array[j]
                j = j-1
            input_array[j+1] = key
        else:
            while j>=0 and (key < input_array[j]):
                input_array[j+1] = input_array[j]
                j = j-1
            input_array[j+1] = key      
    
    # return input_array

def merge_sort(input_array):
    if len(input_array)>1:
        # 1) Divide into small subproblems
        mid = len(input_array)//2
        L = input_array[:mid]
        R = input_array[mid:]

        # 2) Conquer each subproblem Recursively
        merge_sort(L)
        merge_sort(R)

        # 3) Merge routine    
        i = 0
        j = 0
        k = 0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                input_array[k]=L[i]
                i+=1
            else:
                input_array[k]=R[j]
                j+=1
            k+=1
        while i < len(L): 
            input_array[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            input_array[k] = R[j] 
            j+= 1
            k+= 1

if __name__ == "__main__":

    arr = [8,7,6,5,4,3,2,1]

    # # Insertion Sort
    # print("The Input Array \t\t= {}".format(arr))
    # mode = 'Ascending'
    # insertion_sort(arr,mode)
    # print("{} Output Array \t\t= {}".format(mode, arr))
    # mode = 'Descending'
    # insertion_sort(arr,mode)
    # print("{} Output Array \t= {}".format(mode, arr))

    # Merge Sort
    print("Input  = {}".format(arr))
    merge_sort(arr)
    print("Output = {}".format(arr))
    