import random

# Partition function that rearranges the array around a pivot
def partition(arr, low, high):
    # Choose a random pivot index
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    
    # Swap the pivot element with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    # Partitioning step
    i = low - 1  # i will mark the boundary for smaller elements
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap smaller element to the left side
    
    # Swap the pivot element into its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1  # Return the pivot index

# Randomized Quick Sort function
def randomized_quick_sort(arr, low, high):
    if low < high:
        # Get the pivot index after partitioning
        pivot_index = partition(arr, low, high)
        
        # Recursively sort the left and right subarrays
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

# Driver function to sort the array
def quick_sort(arr):
    randomized_quick_sort(arr, 0, len(arr) - 1)
    return arr

# Example usage:
arr = [0, 10, 25, 100, 999, 10000, 2000000]
print("Original Array:", arr)
sorted_arr = quick_sort(arr)
print("Sorted Array:", sorted_arr)
