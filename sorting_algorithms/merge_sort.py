import timeit

from sorting_algorithms.utils import generate_random_array


def merge_sort(arr):
    if len(arr) <= 1:
        return
    # ділимо на 2 масиви Lівий і R Правий
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]

    # кожен з них сортуємо
    merge_sort(L)
    merge_sort(R)

    i = j = k = 0
    # алгоритм злиття
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


if __name__ == "__main__":
    # Generate a random array of size 1000 for testing
    arr = generate_random_array(1000)

    # Measure the time taken to sort the array using merge sort
    time_taken = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)

    print("Time taken to sort array of size 1000 with merge sort:", time_taken, "seconds")
