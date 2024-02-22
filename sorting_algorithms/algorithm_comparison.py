import timeit

from sorting_algorithms.tim_sort import tim_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.utils import generate_sorted_array, generate_random_array, generate_reverse_sorted_array

if __name__ == '__main__':
    for size in [100, 1_000, 10_000]:
        for arr_gen, arr_gen_name in zip(
                [generate_random_array,    generate_sorted_array,   generate_reverse_sorted_array],
                ["generate_random_array", "generate_sorted_array", "generate_reverse_sorted_array"]
        ):
            print(f"{arr_gen_name=}")
            arr = arr_gen(size)
            for sort_alg, sort_alg_name in zip(
                    [insertion_sort,    merge_sort,       tim_sort       ],
                    ["Insertion sort", "Merge sort    ", "Timsort       "]
            ):
                time_taken = timeit.timeit(lambda: sort_alg(arr.copy()), number=5)
                print(f"Time taken to sort array of size {size} with {sort_alg_name} in seconds: {time_taken:.5f}")
        print("-----------------------------------------------------------------")
