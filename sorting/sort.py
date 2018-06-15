def sort_by_insertion_sort(input_sequence):
    for i in xrange(1, len(input_sequence)):
        key = input_sequence[i]
        # insert key in the sorted range of 0 to i-1
        j = i - 1
        while input_sequence[j] > key and j >= 0:
            input_sequence[j + 1] = input_sequence[j]
            j = j - 1
        input_sequence[j + 1] = key