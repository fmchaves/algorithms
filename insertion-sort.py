# Implement Insertion Sort
# The next sorting method we'll look at is insertion sort. This method works by building up a sorted array at the beginning of the list.
# It begins the sorted array with the first element. Then it inspects the next element and swaps it backwards into the sorted array until it is in sorted position.
# It continues iterating through the list and swapping new items backwards into the sorted portion until it reaches the end.
# This algorithm has quadratic time complexity in the average and worst cases.

# Instructions: Write a function insertionSort which takes an array of integers as input and returns an array of these integers in sorted order from least to greatest.

def insertion_sort(array: list, ascending=True) -> list:
    """This function sort an array implementing the insertion sort method    

    Parameters
    ----------
    array : list
        A list containing the elements to be sorted
    ascending : boolen
        Indicates whether to sort in ascending order

    Returns
    -------
    list
        A sorted list
    """

    list_len = len(array)

    if list_len > 1:
        for i in range(1, list_len):
            for j in range(i, 0, -1):
                if ascending and array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                elif not ascending and array[j] > array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                else:
                    break
    return array


assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4,
                                           5], 'The sorted array should be [1,2,3,4,5]'
assert insertion_sort([1, 2, 3, 4, 5], False) == [
    5, 4, 3, 2, 1], 'The sorted array should be [5,4,3,2,1]'
