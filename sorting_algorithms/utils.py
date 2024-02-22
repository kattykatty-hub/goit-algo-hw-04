import random


def generate_random_array(size):
    return [random.randint(0, size) for _ in range(size)]


def generate_sorted_array(size):
    return sorted([random.randint(0, size) for _ in range(size)])


def generate_reverse_sorted_array(size):
    return sorted([random.randint(0, size) for _ in range(size)], reverse=True)
