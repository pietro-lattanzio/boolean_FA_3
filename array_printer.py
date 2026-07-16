def print_array_error_even(array):
    if len(array) % 2 != 0:
        raise ValueError("Array length must be even.")
    print("Array:", array)