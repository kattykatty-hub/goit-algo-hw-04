import timeit

from sorting_algorithms.utils import generate_random_array


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    # Generate a random array of size 1000 for testing
    arr = generate_random_array(1000)

    # Measure the time taken to sort the array using insertion sort
    time_taken = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)

    print("Time taken to sort array of size 1000 with insertion sort:", time_taken, "seconds")
