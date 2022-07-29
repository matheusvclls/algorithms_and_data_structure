
def merge_sort(arr):
    print("Function: Call merge_sort")

    # Check if array has more than 1 element
    if len(arr) <= 1:
        print('End')
        return 
    # Divide the array and get only the integer
    mid = len(arr)//2

    # Set left and right list
    left_list = arr[:mid]
    right_list = arr[mid:]
    print('left list: {}'.format(left_list))
    print('right list: {}'.format(right_list))
    print('\n')

    # Apply merge sort again in both lists
    merge_sort(left_list)
    merge_sort(right_list)

    merge_two_sorted_lists(left_list, right_list, arr)

def merge_two_sorted_lists(left_list,right_list,arr):
    print("\nFunction: Call merge_two_sorted_lists:")
    len_left_list = len(left_list)
    len_right_list = len(right_list)

    pointer_left = pointer_right = pointer_new_list = 0

    while pointer_left < len_left_list and pointer_right < len_right_list:
        if left_list[pointer_left] <= right_list[pointer_right]:
            arr[pointer_new_list] = left_list[pointer_left]
            pointer_left+=1
        else:
            arr[pointer_new_list] = right_list[pointer_right]
            pointer_right+=1   
        pointer_new_list+=1

    while pointer_right < len_right_list: 
        arr[pointer_new_list] = right_list[pointer_right]
        pointer_right+=1
        pointer_new_list+=1

    while pointer_left < len_left_list:
        arr[pointer_new_list] = left_list[pointer_left]
        pointer_left+=1
        pointer_new_list+=1
    
    print("sorted list: {}".format(arr))

x = [4,6,7,3,5,8,0,24,44444,5]
merge_sort(x)
print(x)