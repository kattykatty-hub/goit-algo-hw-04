import timeit

from sorting_algorithms.utils import generate_random_array

MIN_MERGE = 32


def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = arr[l:m + 1], arr[m + 1:r + 1]
    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1


def tim_sort(arr):
    n = len(arr)
    for i in range(0, n, MIN_MERGE):
        insertion_sort(arr, i, min((i + MIN_MERGE - 1), (n - 1)))

    curr_size = MIN_MERGE
    while curr_size < n:
        for left in range(0, n, 2 * curr_size):
            mid = left + curr_size - 1
            right = min((left + 2 * curr_size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        curr_size *= 2


if __name__ == "__main__":
    # Generate a random array of size 1000 for testing
    arr = generate_random_array(1000)

    # Measure the time taken to sort the array using Timsort (Python's built-in sorted function)
    time_taken = timeit.timeit(lambda: sorted(arr.copy()), number=1)

    print("Time taken to sort array of size 1000 with Timsort:", time_taken, "seconds")
