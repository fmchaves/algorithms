# Implement Selection Sort
# Here we will implement selection sort. Selection sort works by selecting the minimum value in a list and swapping
# it with the first value in the list. It then starts at the second position, selects the smallest value in the remaining list,
# and swaps it with the second element. It continues iterating through the list and swapping elements until it reaches the end of the list.
# Now the list is sorted. Selection sort has quadratic time complexity in all cases.

# Instructions: Write a function selectionSort which takes an array of integers as input and returns an array of
# these integers in sorted order from least to greatest.

def selection_sort(array: list, ascending: bool = True) -> list:
    '''
    Sort an array using the selection sort method.

    Parameters:
    ----------
        array: list
            A list containing the elements.
        ascending: bool (default True)
            A boolean value indicating where to sort the list in ascending or descending order.

    Returns:
    --------
        A sorted list

    Raises:
    -------
        TypeError: if one of the input parameters do not have the right type.
    '''

    # Checks whether the array has the correct type
    if not isinstance(array, list):
        raise TypeError('array parameter should be a list')

    # Checks whether the ascending parameter has the correct type
    if not isinstance(ascending, bool):
        raise TypeError('ascending parameters should be a boolean')

    n = len(array)
    if n:
        # The following block of code will sort the array based on the selection sort method
        for i in range(0, n - 1):
            ref_idx = i
            for j in range(i + 1, n):
                if ascending and array[j] < array[ref_idx]:
                    ref_idx = j
                elif not ascending and array[j] > array[ref_idx]:
                    ref_idx = j
            if ref_idx != i:
                array[i], array[ref_idx] = array[ref_idx], array[i]
    return array


assert selection_sort([4, 1, 5, 3, 2], True) == [1, 2, 3, 4, 5], ValueError(
    'The sorted array should be equal to [1, 2, 3, 4, 5]')

assert selection_sort([4, 1, 5, 3, 2], False) == [5, 4, 3, 2, 1], ValueError(
    'The sorted array should be equal to [5, 4, 3, 2, 1]')
