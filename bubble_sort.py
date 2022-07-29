numbers_list = [90,1,20,31,2,8,54,6]


def bubble_sort(list_to_sort: list) -> list:
    """
    Implement the bubble sort algorithm in Python
    """

    # Get lenght of the list
    len_list = len(list_to_sort)

    # Iterate in len -1 elem times
    for i in range(len_list-1):

        # Bubble short always compare the current index with the next one
        if list_to_sort[i] > list_to_sort[i+1]:
            aux = list_to_sort[i]
            list_to_sort[i] = list_to_sort[i+1]
            list_to_sort[i+1] = aux

    print(list_to_sort)
    return list_to_sort


bubble_sort(numbers_list)