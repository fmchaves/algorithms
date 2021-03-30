# Pairwise
# Given an array arr, find element pairs whose sum equal the second argument arg and return the sum of their indices.
# You may use multiple pairs that have the same numeric elements but different indices.
# Each pair should use the lowest possible available indices.
# Once an element has been used it cannot be reused to pair with another element.
# For instance, pairwise([1, 1, 2], 3) creates a pair[2, 1] using the 1 at index 0 rather than the 1 at index 1, because 0+2 < 1+2.

# For example pairwise([7, 9, 11, 13, 15], 20) returns 6.
# The pairs that sum to 20 are[7, 13] and [9, 11].
# We can then write out the array with their indices and values.

# Index	0	1	2	3	4
# Value	7	9	11	13	15

# Below we'll take their corresponding indices and add them.

# 7 + 13 = 20 → Indices 0 + 3 = 3
# 9 + 11 = 20 → Indices 1 + 2 = 3
# 3 + 3 = 6 → Return 6

def pairwise(arr, arg):

    # Check the type of the arguments
    if not isinstance(arr, list):
        raise TypeError('arr should be a list')
    if not isinstance(arg, int):
        raise TypeError('arg should be an integer')

    arr = [(idx, value) for idx, value in enumerate(arr)]
    arr = sorted(arr, key=lambda pair: pair[1])

    # Sum of indexes
    sum_idx = 0

    for i in range(len(arr)):
        if arr[i][1] > arg:
            break
        else:
            for j in range(i + 1, len(arr)):
                pair_sum = arr[i][1] + arr[j][1]
                if pair_sum > arg:
                    break
                elif pair_sum == arg:
                    sum_idx += arr[i][0] + arr[j][0]
    return sum_idx


if __name__ == '__main__':

    v = [7, 9, 11, 13, 15]
    print(pairwise(v, 20))
