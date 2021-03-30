# Inventory Update

# Compare and update the inventory stored in a 2D array against a second 2D array
# of a fresh delivery. Update the current existing inventory item quantities (in arr1).
# If an item cannot be found, add the new item and quantity into the inventory array.
# The returned inventory array should be in alphabetical order by item.


def update_inventory1(arr1: list, arr2: list):
    
    # Check the type of the arguments
    for var_name, var_value in {'arr1': arr1, 'arr2': arr2}.items():
        if not isinstance(var_value, list):
            raise TypeError(f'{var_name} should be an instance of list.')

    # Converting list to dictionary
    arr1 = dict([(key, value) for value, key in arr1])
    arr2 = dict([(key, value) for value, key in arr2])

    # Updating itens
    for key, value in arr2.items():
        arr1[key] = arr1.get(key, 0) + value

    # Converting the dictionary to list and sorting the itens by name
    return sorted([[value, key] for key, value in arr1.items()], key=lambda pair: pair[1])



if __name__ == '__main__':

    curInv = [
        [21, "Bowling Ball"],
        [2, "Dirty Sock"],
        [1, "Hair Pin"],
        [5, "Microphone"]
    ]

    newInv = [
        [2, "Hair Pin"],
        [3, "Half-Eaten Apple"],
        [67, "Bowling Ball"],
        [7, "Toothpaste"]
    ]
    
    # Test case
    assert update_inventory1(curInv, newInv) == [[88, "Bowling Ball"], [2, "Dirty Sock"], [3, "Hair Pin"], [3, "Half-Eaten Apple"], [5, "Microphone"], [7, "Toothpaste"]], ValueError('Invetories are different.')    