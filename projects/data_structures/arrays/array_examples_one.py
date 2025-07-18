# Largest element in an array

def largest_element_of_array(arr):
    largest_element = arr[0]
    for item in arr:
        if item > largest_element:
            largest_element = item
    return largest_element

def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    largest = largest_element_of_array(array)
    print(largest)

if __name__ == '__main__':
    main()