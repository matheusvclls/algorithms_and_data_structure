list_numbers = [6,7,98,343,65,3,5,6,0]


def quick_sort(list_to_sort):
    length = len(list_to_sort)
    if length < 1:
        return list_to_sort
    else:
        pivot = list_to_sort.pop()

    items_greater_than_pivot = []
    items_lower_than_pivot = []

    for item in list_to_sort:
        if item > pivot:
            items_greater_than_pivot.append(item)
        else:
            items_lower_than_pivot.append(item)

    return quick_sort(items_lower_than_pivot) + [pivot] + quick_sort(items_greater_than_pivot)

print(quick_sort(list_numbers))