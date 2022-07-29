numbers_list = [90,1,20,31,2,8,54,6]

def selection_sort(list_to_sort : list):
    """
    Implement the selection sort algorithm in Python
    """

    print(list_to_sort, ' - original list')

    # Get lenght of the list
    len_list = len(list_to_sort)

    # Iterate in all list
    for current_pointer_list in range(len_list-1):

        # Minimum index accepted is in the current pointer 
        minimum_number_index = current_pointer_list

        # Iterate in all list without the first ones which is already ordered
        for current_index in range(current_pointer_list, len_list):
        
            # Check if current number is smaller than minimum
            if list_to_sort[current_index] < list_to_sort[minimum_number_index]:
                minimum_number_index = current_index
        
        # Replace number if there is one smaller in the loop
        if list_to_sort[current_pointer_list] > list_to_sort[minimum_number_index]:
            aux = list_to_sort[current_pointer_list] # Store in a aux variable the old elem
            list_to_sort[current_pointer_list] = list_to_sort[minimum_number_index] # Set the new minimum
            list_to_sort[minimum_number_index] = aux # Repĺace in the position of the new minimum

    print(list_to_sort, ' - list sorted')
    
    return list_to_sort


selection_sort(numbers_list)