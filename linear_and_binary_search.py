
def check_index(index: int):
    if index is not None:
        print('Target found index: {}'.format(index))
    
    else:
        print('Target not found in list')

def linear_search(list: list, target):
    '''
    Method for finding an element within a list. It sequentially checks each element 
    of the list until a match is found or the whole list has been searched
    '''

    for i in range(0, len(list)):

        if list[i]== target:
            return i
    return None

def binary_search(list:list, target):
    '''
    Binary search is an efficient algorithm for finding an item from a sorted list of items. 
    It works by repeatedly dividing in half the portion of the list that could contain the item, 
    until you've narrowed down the possible locations to just one
    '''
    first = 0
    last = len(list) -1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint]<target:
            first = midpoint + 1
        else:
            last = midpoint -1
    return None


sequence_of_numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(sequence_of_numbers, 20)
check_index(result)


result = binary_search(sequence_of_numbers, 3)
check_index(result)
