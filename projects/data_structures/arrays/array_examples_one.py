# Largest element in an array

# --------------------------------------------------------------------------------
# Iterative approach
def largest_element_iterative(arr):
    largest_element = arr[0]
    for item in arr:
        if item > largest_element:
            largest_element = item
    return largest_element

# --------------------------------------------------------------------------------
# Recursive approach
def largest_element_recursive(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        first_element = arr[0]
        max_of_rest = largest_element_recursive(arr[1:])
        if max_of_rest is None:
            return first_element
        elif max_of_rest < first_element:
            return first_element
        else:
            return max_of_rest

def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(largest_element_iterative(array))
    print(largest_element_recursive(array))

if __name__ == '__main__':
    main()