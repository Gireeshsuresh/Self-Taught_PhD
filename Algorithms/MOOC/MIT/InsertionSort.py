array_input = [ 8, 2, 4, 9, 3, 6]

def insertion_sort(input_array, mode):
    """
    Given an Array as input, perform Insertion Sort on the given array
    """
    for i in range(1, len(array_input)):
        key = array_input[i]
        j = i-1

        if mode =='Descending':
            while j>=0 and (key > array_input[j]):
                array_input[j+1] = array_input[j]
                j = j-1
            array_input[j+1] = key
        else:
            while j>=0 and (key < array_input[j]):
                array_input[j+1] = array_input[j]
                j = j-1
            array_input[j+1] = key      
    
    return array_input



print("The Input Array \t\t= {}".format(array_input))

mode = 'Ascending'
sorted_array = insertion_sort(array_input,mode)
print("{} Output Array \t\t= {}".format(mode, sorted_array))


mode = 'Descending'

sorted_array = insertion_sort(array_input,mode)
print("{} Output Array \t= {}".format(mode, sorted_array))
