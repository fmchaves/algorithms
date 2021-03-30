# Implement Bubble Sort

# This is the first of several challenges on sorting algorithms.
# Given an array of unsorted items, we want to be able to return a sorted array.
# We will see several different methods to do this and learn some tradeoffs between these different approaches.
# While most modern languages have built-in sorting methods for operations like this,
# it is still important to understand some of the common basic approaches and learn how they can be implemented.

# Here we will see bubble sort. The bubble sort method starts at the beginning of an unsorted
# array and 'bubbles up' unsorted values towards the end, iterating through the array until it
# is completely sorted. It does this by comparing adjacent items and swapping them if they are out of order.
# The method continues looping through the array until no swaps occur at which point the array is sorted.

# This method requires multiple iterations through the array and for average and worst cases has quadratic
# time complexity. While simple, it is usually impractical in most situations.

# Instructions: Write a function bubbleSort which takes an array of integers as input and
# returns an array of these integers in sorted order from least to greatest.

def bubble_sort(array, ascending=True):
    '''
    Sort an array using the bubble sort method.

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

    # Checks if the array parameters is a list
    if not isinstance(array, list):
        raise TypeError('array parameter must be a list')

    # Checks if the ascending parameters is a boolean
    if not isinstance(ascending, bool):
        raise TypeError('ascending parameter must be a boolen')

    n = len(array)
    if n:
        # The following block of code will sort the array based on the bubble sort method
        for i in range(1, n - 1):
            for j in range(n - i):
                if ascending and array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                elif not ascending and array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    return array


assert bubble_sort([4, 1, 5, 3, 2], True) == [1, 2, 3, 4, 5], ValueError(
    'The sorted array should be equal to [1, 2, 3, 4, 5]')

assert bubble_sort([4, 1, 5, 3, 2], False) == [5, 4, 3, 2, 1], ValueError(
    'The sorted array should be equal to [5, 4, 3, 2, 1]')
