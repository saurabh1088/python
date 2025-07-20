# Largest element in an array

# --------------------------------------------------------------------------------
# Iterative approach
# Time Complexity - O(n)
# Space Complexity - O(1)
def largest_element_iterative(arr):
    largest_element = arr[0]
    for item in arr:
        if item > largest_element:
            largest_element = item
    return largest_element

# --------------------------------------------------------------------------------
# Recursive approach
# Time Complexity - O(n^2)
# Each recursive call creates a new list slice (arr[1:]), which costs O(k) time
# where k is the slice's length, leading to a sum of O(n) + O(n-1) + ... + O(1)
# operations.
#
# Space Complexity - O(n)
# The recursion depth is O(n) (for the call stack), and each recursive call creates
# a new list slice that temporarily exists in memory, cumulatively consuming O(n)
# space. The operation arr[1:] creates a new list object in memory for each recursive
# call. While Python's garbage collector will eventually reclaim these, at any given
# point in time, there will be n distinct list objects (the original list and n-1
# slices of decreasing size) held in memory on the call stack. The total memory
# consumed by these concurrently existing slices is proportional to n. This also
# contributes O(n) space.
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

# --------------------------------------------------------------------------------
# Main
def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(largest_element_iterative(array))
    print(largest_element_recursive(array))

if __name__ == '__main__':
    main()