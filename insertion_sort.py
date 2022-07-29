numbers_list = [90,1,20,31,2,8,54,6]

def insertion_sort(list_to_sort):
    
    # Get len list
    len_list = len(list_to_sort)

    for i in range(1, len_list):
        value_to_sort = list_to_sort[i]

        while list_to_sort[i-1] > value_to_sort and i>0:
            aux = list_to_sort[i-1]
            list_to_sort[i-1] = list_to_sort[i]
            list_to_sort[i] = aux

            i = i-1

    return list_to_sort


print(insertion_sort([90,1,20,31,2,8,54,6]))
